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

update_product_price(Products, "matcha", 30)
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
remove_product(Products , "latte")
print(Products)