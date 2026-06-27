import pandas as pd


def clean_sales_data(sales_df):
    dup_count = sales_df.duplicated().sum()
    print("Duplicate rows found and removed:", dup_count)

    sales_df = sales_df.drop_duplicates().copy()

    sales_df["quantity"] = sales_df["quantity"].fillna(0)

    sales_df = sales_df.dropna(subset=["amount"]).copy()

    print("Cleaned sales_df shape:", sales_df.shape)
    print(sales_df.head(), end="\n\n")

    return sales_df


def convert_types(sales_df):
    sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"], errors="coerce")
    sales_df["amount"] = pd.to_numeric(sales_df["amount"], errors="coerce").astype(float)

    return sales_df


def main():
    sales_df = pd.read_csv("sales_data.csv")

    sales_df = clean_sales_data(sales_df)
    sales_df = convert_types(sales_df)

    print("After type conversion:")
    print(sales_df.dtypes)


if __name__ == "__main__":
    main()