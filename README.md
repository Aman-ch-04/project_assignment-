# Retail Sales Data Pipeline

## Project Overview

This project was developed as part of a Data Engineering assignment. The objective was to build a simple ETL (Extract, Transform, Load) pipeline that processes raw retail sales data, cleans it, transforms it into meaningful information, and stores it in a SQLite database for reporting.

The project demonstrates data ingestion, data cleaning, transformation, SQL integration, reporting, and error handling using Python.

---

## Problem Statement

RetailMart Pvt. Ltd. collects daily sales data from multiple stores across India. The data is stored in CSV files and may contain missing values, duplicate records, and incorrect data types.

The objective of this project is to:

* Load data from multiple CSV files.
* Clean and preprocess the data.
* Merge different datasets.
* Calculate business metrics.
* Store the processed data into a SQLite database.
* Generate reports using SQL.
* Build an automated pipeline with error handling.

---

## Dataset

The project uses three CSV files:

### sales_data.csv

Contains daily sales transactions.

Columns:

* sale_id
* store_id
* product_id
* quantity
* sale_date
* amount

### products.csv

Contains product information.

Columns:

* product_id
* product_name
* category
* price

### stores.csv

Contains store details.

Columns:

* store_id
* store_name
* city
* region

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite (sqlite3)
* SQL

---

## Project Structure

```text
Retail-Sales-Data-Pipeline/
│
├── sales_data.csv
├── products.csv
├── stores.csv
├── retail_sales.sqlite
│
├── task1_data_ingestion.py
├── task2_data_cleaning.py
├── task3_data_transformation.py
├── task4_data_loading_sql.py
├── task5_reporting_insights_sql.py
├── task6_pipeline_error_handling.py
│
├── README.md
└── requirements.txt
```

---

## Tasks Completed

### Task 1 – Data Ingestion

* Loaded all CSV files using Pandas.
* Displayed dataset shape and first five rows.
* Checked for missing values.

### Task 2 – Data Cleaning

* Removed duplicate records.
* Filled missing values in the quantity column.
* Removed rows with missing amount.
* Converted columns to appropriate data types.

### Task 3 – Data Transformation

* Merged sales, product, and store datasets.
* Created a new column `total_revenue`.
* Calculated mean, maximum, and minimum revenue.
* Generated city-wise revenue summary.

### Task 4 – Data Loading

* Loaded the processed data into a SQLite database.
* Created the `retail_sales` table.
* Executed SQL queries to retrieve business information.

### Task 5 – Reporting & Insights

Generated reports for:

* Total number of transactions
* Total revenue
* Top-selling city
* Top-selling product
* Revenue per store per day

### Task 6 – Pipeline & Error Handling

* Created a reusable `run_pipeline()` function.
* Added exception handling using `try-except`.
* Displayed appropriate error messages if any input file is missing.

---

## ETL Workflow

```text
CSV Files
    │
    ▼
Data Ingestion
    │
    ▼
Data Cleaning
    │
    ▼
Data Transformation
    │
    ▼
SQLite Database
    │
    ▼
SQL Reporting
```

---

## Skills Demonstrated

* ETL Pipeline Development
* Data Cleaning
* Data Transformation
* SQL Queries
* Database Integration
* Python Programming
* Pandas
* NumPy
* SQLite
* Error Handling

---

## Future Improvements

* Automate the pipeline using Apache Airflow.
* Store data in PostgreSQL instead of SQLite.
* Containerize the project using Docker.
* Build dashboards using Power BI or Tableau.
* Deploy the pipeline on AWS.

---

## Author

**Aman Choudhary**

B.Tech Computer Science & Engineering

GitHub: *(Add your GitHub profile link here)*
