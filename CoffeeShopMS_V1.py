Products=[]
def add_product(Products, product_id, name, price):
    valid_name = name.strip()
    normalized_name = valid_name.lower()
   
    if price <= 0 : # price is valid
        return False
    if valid_name == "": # name null
        return False
    for product in Products:
        if product["name"].lower() == normalized_name :# name exsist
            return False
        
    new_product = {"id": product_id ,"name": normalized_name.title() , "price": price}
    Products.append(new_product)
    return True
            
add_product(Products, 1, "Matcha", 25)   # True
add_product(Products, 2, "Latte", 18)    # True
add_product(Products, 3, "MATCHA", 20)   # False
add_product(Products, 4, "   ", 20)     # False

print(Products)

def find_product(Products, name):
    valid_name = name.strip().lower()
    for product in Products:
        if product["name"].lower() == valid_name:
            return product
    return None

#print(find_product(Products, "matcha"))
#print(find_product(Products, "coffee"))

def update_product_price(Products, name, new_price):
    valid_name = name.strip().lower()
    for product in Products:
        if product["name"].lower() == valid_name:
            if new_price > 0:
                product["price"] = new_price
                return True
            return False
    return False

#update_product_price(Products, "matcha", 30)
#print(update_product_price(Products, "Coffee", 20))  # False
#print(update_product_price(Products, "Matcha", -5))  # False
#print(Products)

def remove_product(Products, name):
    valid_name = name.strip().lower()
    for product in Products:
        if product["name"].lower()== valid_name:
            Products.remove(product)
            return True
    return False
#remove_product(Products , "latte")
#print(Products)

def find_product_by_id(Products, product_id):
    for product in Products:
        if product["id"] == product_id:
            return product
    return None
print(find_product_by_id(Products, 1))
print(find_product_by_id(Products, 99))


def calculate_item_total(Products, product_id, quantity):
    item = find_product_by_id(Products , product_id)
    if item is None:
        return False
    if quantity <= 0:
        return False
    total = item["price"] * quantity
    return total
print(calculate_item_total(Products, 1, 3))

order_items =[]
def create_order_item(Products, product_id, quantity):
    item = find_product_by_id(Products , product_id)
    if item is None:
        return None
    if quantity <= 0 :
        return None
    total = calculate_item_total(Products , product_id , quantity)
    new_order = {"product_id": product_id , "name": item["name"] , "quantity": quantity , "total": total}
    order_items.append(new_order)
    return new_order
create_order_item(Products, 1, 2)
create_order_item(Products, 2, 1)
print(order_items)

def calculate_order_total(order_items):
    total=0 
    for order in order_items:
        total += order["total"] 
    return total
print(calculate_order_total(order_items))