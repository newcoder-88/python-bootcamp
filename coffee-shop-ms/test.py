from orders import validate_order , validate_quantity

data = {
    "Products": [
        {"id": 1, "name": "Latte", "price": 18},
        {"id": 2, "name": "Espresso", "price": 12},
        {"id": 3, "name": "Cappuccino", "price": 20}
    ]
}



try:
    validate_quantity(0)
except ValueError:
    print("test passed : invalid quantity rejected")
else:
    raise AssertionError("expected ValueError")