# Products ordered data structures
products_ordered1 = [
    {
        'productName': 'productName1',
        'productBrand': 'productBrand1',
        'productQuantity': 1,
        'computedPrice': 100.0,
        'BLOB': 'BLOB1'
    },
    {
        'productName': 'productName2',
        'productBrand': 'productBrand2',
        'productQuantity': 2,
        'computedPrice': 200.0,
        'BLOB': 'BLOB2'
    }
]

products_ordered2 = [
    {
        'productName': 'productName3',
        'productBrand': 'productBrand3',
        'productQuantity': 3,
        'computedPrice': 300.0,
        'BLOB': 'BLOB3'
    },
    {
        'productName': 'productName4',
        'productBrand': 'productBrand4',
        'productQuantity': 4,
        'computedPrice': 400.0,
        'BLOB': 'BLOB4'
    }
]

# List of products ordered
all_products_ordered = [products_ordered1, products_ordered2]

# Orders list data structure
orders_list = [
    {
        'products_ordered': products_ordered1,
        'buyerName': 'Buyer1',
        'buyerContact': 'Contact1',
        'totalRevenue': 600.0,
        'date': '2023-06-26',
        'timestamp': '12:00:00'
    },
    {
        'products_ordered': products_ordered2,
        'buyerName': 'Buyer2',
        'buyerContact': 'Contact2',
        'totalRevenue': 900.0,
        'date': '2023-06-27',
        'timestamp': '14:00:00'
    }
]

# Printing all_products_ordered
print("All Products Ordered:")
for i, products in enumerate(all_products_ordered, start=1):
    print(f"\nOrder {i}:")
    for product in products:
        print(product)

# Printing orders_list with new line separators
print("\nOrders List:")
for order in orders_list:
    print(f"Order:")
    print(f"Products Ordered:")
    for product in order['products_ordered']:
        print(product)
    print(f"Buyer Name: {order['buyerName']}")
    print(f"Buyer Contact: {order['buyerContact']}")
    print(f"Total Revenue: {order['totalRevenue']}")
    print(f"Date: {order['date']}")
    print(f"Timestamp: {order['timestamp']}")
    print()  # Adding a new line for better readability