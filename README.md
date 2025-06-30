# ETL Project with Python, Pandas, and PostgreSQL

This project demonstrates a simple **ETL (Extract - Transform - Load)** pipeline using:

- Python
- Pandas
- PostgreSQL
- Fake data with `Faker`

#ETL Flow 


1.Extract
- Generate fake `customers`, `products`, and `orders` using the `Faker` library.

2.Transform
- Merge dataframes
- Add `quantity`, compute `total_price`
- Format dates and organize columns

3.Load
- Push the final cleaned dataset to a PostgreSQL table using `SQLAlchemy`.

