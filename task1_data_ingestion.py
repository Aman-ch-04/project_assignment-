import pandas as pd


def load_data():
    sales_path = "sales_data.csv"
    products_path = "products.csv"
    stores_path = "stores.csv"

    sales_df = pd.read_csv(sales_path)
    products_df = pd.read_csv(products_path)
    stores_df = pd.read_csv(stores_path)

    print("sales_data.csv shape:", sales_df.shape)
    print(sales_df.head(), end="\n\n")

    print("products.csv shape:", products_df.shape)
    print(products_df.head(), end="\n\n")

    print("stores.csv shape:", stores_df.shape)
    print(stores_df.head(), end="\n\n")

    # Missing value summary
    print("Missing values summary:")
    print("--- sales_df ---")
    print(sales_df.isna().sum())
    print("--- products_df ---")
    print(products_df.isna().sum())
    print("--- stores_df ---")
    print(stores_df.isna().sum())

    return sales_df, products_df, stores_df


if __name__ == "__main__":
    load_data()

