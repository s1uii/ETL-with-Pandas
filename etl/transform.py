import pandas as pd


def transform(customers, products, orders):
    orders_customers = orders.merge(customers, on='customer_id', how='left')

    full_data = orders_customers.merge(products, on='product_id', how='left')

    full_data['total_price'] = full_data['quantity'] * full_data['product_price']

    full_data['order_date'] = pd.to_datetime(full_data['order_date'])

    full_data = full_data[[
        'order_id', 'order_date',
        'customer_id', 'name', 'email', 'city',
        'product_id', 'product_name', 'product_type', 'product_price',
        'quantity', 'total_price'
    ]]
    return full_data