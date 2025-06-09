
import pandas as pd
import numpy as np
from faker import Faker
import random

def generate_ecommerce_dataset(n_customers=1000, n_orders=3000, n_products=200,
                                min_items_per_order=1, max_items_per_order=5, seed=42):
    fake = Faker()
    np.random.seed(seed)
    random.seed(seed)
    Faker.seed(seed)

    product_categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys', 'Beauty', 'Grocery']
    payment_methods = ['Credit Card', 'PayPal', 'Gift Card', 'Bitcoin']
    device_types = ['Mobile', 'Desktop', 'Tablet']
    locations = ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Washington', 'Arizona']

    # Generate Customers
    customer_ids = [f"CUST{i:05d}" for i in range(1, n_customers + 1)]

    # Generate Products Table
    product_ids = [f"PROD{i:05d}" for i in range(1, n_products + 1)]
    products_df = pd.DataFrame({
        "ProductID": product_ids,
        "ProductCategory": [np.random.choice(product_categories) for _ in range(n_products)],
        "ProductName": [fake.catch_phrase() for _ in range(n_products)],
        "BasePrice": np.round(np.random.uniform(5, 500, size=n_products), 2)
    })

    # Generate Orders Table
    order_ids = [f"ORD{i:05d}" for i in range(1, n_orders + 1)]
    orders_df = pd.DataFrame({
        "OrderID": order_ids,
        "CustomerID": np.random.choice(customer_ids, size=n_orders),
        "OrderDate": [fake.date_between(start_date='-2y', end_date='today') for _ in range(n_orders)],
        "CustomerLocation": np.random.choice(locations, size=n_orders),
        "PaymentMethod": np.random.choice(payment_methods, size=n_orders),
        "DeviceType": np.random.choice(device_types, size=n_orders),
    })

    # Generate Order Items (link to products)
    order_items = []
    item_id_counter = 1

    for order_id in order_ids:
        num_items = np.random.randint(min_items_per_order, max_items_per_order + 1)
        for _ in range(num_items):
            product_idx = np.random.randint(0, n_products)
            product = products_df.iloc[product_idx]
            item = {
                "ItemID": f"ITEM{item_id_counter:06d}",
                "OrderID": order_id,
                "ProductID": product["ProductID"],
                "PurchaseAmount": np.round(product["BasePrice"] * np.random.uniform(0.9, 1.2), 2)
            }
            order_items.append(item)
            item_id_counter += 1

    order_items_df = pd.DataFrame(order_items)

    return orders_df, order_items_df, products_df
