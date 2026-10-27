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
   print("valid")
except ValueError as e:
    print(e)


try:
   quantity= validate_quantity(2)
   print("valid quantity:", quantity)
except ValueError as e:
    print(e)


try:
    order= validate_order(data, 2, 3)
    print(order)
except ValueError as e :
    print(e)

try:
    order= validate_order(data, 999, 3)
    print(order)
except ValueError as e :
    print(e)

try:
    order= validate_order(data, 1, -2)
    print(order)
except ValueError as e :
    print(e)
