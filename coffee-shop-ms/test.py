from products import find_product
data = {
    "Products": [
        {"id": 1, "name": "Latte", "price": 15},
        {"id": 2, "name": "Espresso", "price": 10}
    ]
}

print(find_product(data , "Espresso"))