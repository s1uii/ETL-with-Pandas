from etl.extract import generate_fake_data
from etl.transform import transform
from etl.load import load_to_postgres

def main():
    customers, products, orders = generate_fake_data()
    full_data = transform (customers, products, orders)

    db_url = "postgresql://username:password@host:port/database"
    load_to_postgres(full_data, table_name="sales", db_url=db_url)

if __name__ == "__main__":
    main()
