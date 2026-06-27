import os
import sqlite3
import pandas as pd
import numpy as np


def run_pipeline(db_path: str = "retail_sales.sqlite"):
    required_files = ["sales_data.csv", "products.csv", "stores.csv"]
    for f in required_files:
        if not os.path.exists(f):
            print(f"Error: Required file not found: {f}")
            return

    try:
       
        sales_df = pd.read_csv("sales_data.csv")
        products_df = pd.read_csv("products.csv")
        stores_df = pd.read_csv("stores.csv")

        print("Loaded data:")
        print("sales_data shape:", sales_df.shape)
        print("products shape:", products_df.shape)
        print("stores shape:", stores_df.shape)

        
        print("Missing values summary:")
        print("sales_df:\n", sales_df.isna().sum())
        print("products_df:\n", products_df.isna().sum())
        print("stores_df:\n", stores_df.isna().sum())

        
        dup_count = sales_df.duplicated().sum()
        print("Duplicate rows found in sales_data:", dup_count)
        sales_df = sales_df.drop_duplicates().copy()

        sales_df["quantity"] = sales_df["quantity"].fillna(0)
        sales_df = sales_df.dropna(subset=["amount"]).copy()

        sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"], errors="coerce")
        sales_df["amount"] = sales_df["amount"].astype(float)
        sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce").fillna(0).astype(int)

        print("Cleaned sales_df shape:", sales_df.shape)

        
        merged_df = (
            sales_df
            .merge(stores_df, on="store_id", how="inner")
            .merge(products_df, on="product_id", how="inner")
        )

        print("Merged DataFrame shape:", merged_df.shape)
        print("Merged preview:\n", merged_df.head(10))

        merged_df["total_revenue"] = np.multiply(merged_df["quantity"], merged_df["price"])

        print("total_revenue mean/max/min:")
        print(merged_df["total_revenue"].mean(), merged_df["total_revenue"].max(), merged_df["total_revenue"].min())

        city_revenue = (
            merged_df.groupby("city", as_index=False)["total_revenue"]
            .sum()
            .sort_values("total_revenue", ascending=False)
        )
        print("Revenue by city (desc):\n", city_revenue)

        
        con = sqlite3.connect(db_path)
        try:
            merged_df.to_sql("retail_sales", con, if_exists="replace", index=False)
            print(f"Loaded into SQLite table retail_sales: {db_path}")
        finally:
            con.close()

        
        con = sqlite3.connect(db_path)
        try:
            top_products = pd.read_sql_query(
                """
                SELECT
                    product_id,
                    product_name,
                    SUM(quantity) AS total_quantity_sold
                FROM retail_sales
                GROUP BY product_id, product_name
                ORDER BY total_quantity_sold DESC
                LIMIT 3;
                """,
                con,
            )
            print("Top 3 products by quantity sold:\n", top_products)
        finally:
            con.close()

        return merged_df

    except Exception as e:
        # Basic error handling for unexpected failures
        print(f"Pipeline failed with error: {e}")
        return


if __name__ == "__main__":
    run_pipeline()

