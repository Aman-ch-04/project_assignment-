import sqlite3
import pandas as pd


def main():
    # Build cleaned + merged dataset (same logic as in task3)
    sales_df = pd.read_csv("sales_data.csv")
    products_df = pd.read_csv("products.csv")
    stores_df = pd.read_csv("stores.csv")

    sales_df = sales_df.drop_duplicates().copy()
    sales_df["quantity"] = sales_df["quantity"].fillna(0)
    sales_df = sales_df.dropna(subset=["amount"]).copy()

    sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"], errors="coerce")
    sales_df["amount"] = sales_df["amount"].astype(float)
    sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce").fillna(0).astype(int)

    merged_df = (
        sales_df
        .merge(stores_df, on="store_id", how="inner")
        .merge(products_df, on="product_id", how="inner")
    )
    merged_df["total_revenue"] = merged_df["quantity"] * merged_df["price"]

    # Load into SQLite
    db_path = "retail_sales.sqlite"
    con = sqlite3.connect(db_path)
    try:
        merged_df.to_sql("retail_sales", con, if_exists="replace", index=False)
        print(f"Loaded {len(merged_df)} rows into table retail_sales in {db_path}")

        # Top 3 best-selling products by total quantity sold
        query = """
        SELECT
            product_id,
            product_name,
            SUM(quantity) AS total_quantity_sold
        FROM retail_sales
        GROUP BY product_id, product_name
        ORDER BY total_quantity_sold DESC
        LIMIT 3;
        """

        top_products = pd.read_sql_query(query, con)
        print("Top 3 best-selling products by total quantity sold:")
        print(top_products)

    finally:
        con.close()


if __name__ == "__main__":
    main()

