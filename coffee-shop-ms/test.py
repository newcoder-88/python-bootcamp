import orders
data = {
    "Products": [
        {"id": 1, "name": "Latte", "price": 15},
        {"id": 2, "name": "Espresso", "price": 10}
    ],
    "order_items": [],
    "Orders": [],
    "customers": [{"customer_id": 1, "name": "Sarah", "email": "sarah@example.com"}]
}
orders.create_order_item(data,1,2)
orders.create_order_item(data,2,1)
orders.create_order(1 , 1 , data)


orders.remove_order(data, 1)
print(orders.count_orders(data))
print(orders.find_order_by_id(data,1))