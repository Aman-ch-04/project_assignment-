import sqlite3
import pandas as pd


def main():
    db_path = "retail_sales.sqlite"
    con = sqlite3.connect(db_path)
    try:
        # 11. total revenue per store per day
        query_store_day = """
        SELECT
            store_id,
            store_name,
            sale_date,
            SUM(total_revenue) AS total_revenue
        FROM retail_sales
        GROUP BY store_id, store_name, sale_date
        ORDER BY sale_date ASC, store_id ASC;
        """
        store_day = pd.read_sql_query(query_store_day, con)
        print("Total revenue per store per day:")
        print(store_day.head(20), end="\n\n")

        # 12. Python summary report
        total_transactions = pd.read_sql_query("SELECT COUNT(*) AS cnt FROM retail_sales", con)["cnt"].iloc[0]
        total_revenue = pd.read_sql_query("SELECT SUM(total_revenue) AS s FROM retail_sales", con)["s"].iloc[0]

        top_city = pd.read_sql_query(
            """
            SELECT city, SUM(total_revenue) AS city_revenue
            FROM retail_sales
            GROUP BY city
            ORDER BY city_revenue DESC
            LIMIT 1;
            """,
            con,
        )
        top_city_name = top_city["city"].iloc[0]

        top_product = pd.read_sql_query(
            """
            SELECT product_id, product_name, SUM(quantity) AS total_quantity_sold
            FROM retail_sales
            GROUP BY product_id, product_name
            ORDER BY total_quantity_sold DESC
            LIMIT 1;
            """,
            con,
        )
        top_product_name = top_product["product_name"].iloc[0]

        print("--- Summary Report ---")
        print("Total number of transactions:", total_transactions)
        print("Total revenue:", total_revenue)
        print("Top selling city:", top_city_name)
        print("Top selling product:", top_product_name)

    finally:
        con.close()


if __name__ == "__main__":
    main()

