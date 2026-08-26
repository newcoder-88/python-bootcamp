data={
    "Products":[],
    "order_items":[],
    "Orders":[]
    }

# --------------Products--------------
def add_product(data, product_id, name, price):
    valid_name = name.strip()
    normalized_name = valid_name.lower()
   
    if price <= 0 : # price is valid
        return False
    if valid_name == "": # name null
        return False
    for product in data["Products"]:
        if product["name"].lower() == normalized_name :# name exsist
            return False
        
    new_product = {"id": product_id ,"name": normalized_name.title() , "price": price}
    data["Products"].append(new_product)
    return True
            
add_product(data, 1, "Matcha", 25)   # True
add_product(data, 2, "Latte", 18)    # True
add_product(data, 3, "MATCHA", 20)   # False
add_product(data, 4, "   ", 20)     # False

#print(data["Products"])

def find_product(data, name):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower() == valid_name:
            return product
    return None

#print(find_product(data, "matcha"))
#print(find_product(data, "coffee"))

def update_product_price(data, name, new_price):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower() == valid_name:
            if new_price > 0:
                product["price"] = new_price
                return True
            return False
    return False

#update_product_price(data, "matcha", 30)
#print(update_product_price(data, "Coffee", 20))  # False
#print(update_product_price(data, "Matcha", -5))  # False
#print(data["Products"])

def remove_product(data, name):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower()== valid_name:
            data["Products"].remove(product)
            return True
    return False
#remove_product(data , "latte")
#print(data[Products])

def find_product_by_id(data, product_id):
    for product in data["Products"]:
        if product["id"] == product_id:
            return product
    return None
#print(find_product_by_id(data, 1))
#print(find_product_by_id(data, 99))

#--------------Order_items--------------
def calculate_item_total(data, product_id, quantity):
    item = find_product_by_id(data , product_id)
    if item is None:
        return False
    if quantity <= 0:
        return False
    total = item["price"] * quantity
    return total
#print(calculate_item_total(data, 1, 3))


def create_order_item(data, product_id, quantity):
    item = find_product_by_id(data , product_id)
    if item is None:
        return None
    if quantity <= 0 :
        return None
    total = calculate_item_total(data , product_id , quantity)
    new_order = {"product_id": product_id , "name": item["name"] , "quantity": quantity , "total": total}
    data["order_items"].append(new_order)
    return new_order
create_order_item(data, 1, 2)
create_order_item(data, 2, 1)
print(data["order_items"])

def calculate_order_total(data):
    total=0 
    for order in data["order_items"]:
        total += order["total"] 
    return total
#print(calculate_order_total(data))

#--------------Orders--------------
def create_order(order_id, customer_name, data):
    valid_name = customer_name.strip().title()
    if valid_name == "":
        return None
    if len(data["order_items"]) == 0 :
        return None
    order_total =  calculate_order_total(data)
    order_items_copy = data["order_items"].copy()
    new_order= {"order_id": order_id , "customer": valid_name , "items": order_items_copy ,"total": order_total }
    data["Orders"].append(new_order)
    data["order_items"]=[]
    return new_order
create_order(1, "Sarah", data)



def find_order_by_id(data, order_id):
    for order in data["Orders"]:
        if order["order_id"] == order_id:
            return order
    return None
order = find_order_by_id(data, 1)


def remove_order(data, order_id):
    for order in data["Order"]:

        if order["order_id"] == order_id:
            data["Order"].remove(order)
            return True
    return False

def count_orders(data):
    count = 0 
    for order in data["Orders"]:
        count+=1 
    return count
#print(count_orders(data))

print("orders" , data["Orders"])
print("items" , data[ "order_items"])
