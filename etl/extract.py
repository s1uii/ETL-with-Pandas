import random
from faker import Faker
import pandas as pd


def generate_fake_data():
    fake = Faker()

    customers = pd.DataFrame({
        'customer_id': range(1, 51),
        'name': [fake.name() for _ in range(50)],
        'email': [fake.email() for _ in range(50)],
        'city': [fake.city() for _ in range(50)]
    })
    products = pd.DataFrame({
        'product_id': range(1, 51),
        'product_name': [' ' .join(fake.words(nb=2)).title() for _ in range(50)],
        'product_price': [round(random.uniform(10,100),2) for _ in range(50)],
        'product_type': [fake.word().capitalize() for _ in range(50)]
    })
    orders = pd.DataFrame([{
        'order_id': i,
        'customer_id': random.randint(1, 50),
        'product_id': random.randint(1, 20),
        'quantity': random.randint(1, 5),
        'order_date':fake.date_this_year()
    } for i in range(1, 101)])
    return customers, products, orders