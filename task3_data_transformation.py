import pandas as pd
import numpy as np


def main():
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

    merged_df["total_revenue"] = np.multiply(
        merged_df["quantity"],
        merged_df["price"]
    )

    print("Final merged DataFrame:")
    print(merged_df, end="\n\n")

    print("total_revenue stats:")
    print("mean:", np.mean(merged_df["total_revenue"]))
    print("max:", np.max(merged_df["total_revenue"]))
    print("min:", np.min(merged_df["total_revenue"]))
    print()

    city_revenue = (
        merged_df.groupby("city", as_index=False)["total_revenue"]
        .sum()
        .sort_values("total_revenue", ascending=False)
    )

    print("Total revenue per city:")
    print(city_revenue)


if __name__ == "__main__":
    main()