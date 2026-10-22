from products import find_product_by_id, get_valid_product
from customers import find_customer_by_id

def calculate_item_total(data, product_id, quantity):
    item = find_product_by_id(data , product_id)
    if item is None:
        return False
    if quantity <= 0:
        return False
    total = item["price"] * quantity
    return total



def create_order_item(data, product_id, quantity):
    item = find_product_by_id(data , product_id)
    if item is None:
        return None
    if quantity <= 0:
        return None
    total = calculate_item_total(data , product_id , quantity)
    new_order = {"product_id": product_id , "name": item["name"] , "quantity": quantity , "total": total}
    data["order_items"].append(new_order)
    return new_order



def calculate_order_total(data):
    total=0 
    for order in data["order_items"]:
        total += order["total"] 
    return total

def create_order(order_id, customer_id, data):
    if len(data["order_items"]) == 0 :
        return None
     
    if order_id <= 0:
        return None
    order_exists = find_order_by_id(data , order_id)
    if order_exists is not None : 
        return None

    if customer_id <=0 :
        return None   
    customer = find_customer_by_id(data,customer_id)
    if customer is None:
        return None

    
    order_total =  calculate_order_total(data)
    order_items_copy = data["order_items"].copy()

    new_order= {"order_id": order_id ,"customer_id": customer_id , "customer": customer["name"] , "items": order_items_copy ,"total": order_total , "status": "Pending" }
    data["Orders"].append(new_order)
    data["order_items"]=[]
    return new_order


def find_order_by_id(data, order_id):
    for order in data["Orders"]:
        if order["order_id"] == order_id:
            return order
    return None


def find_orders_by_customer(data, customer_id):
    result=[]
    for order in data["Orders"]:
        if order["customer_id"] == customer_id:
            result.append(order)
    return result


def remove_order(data, order_id):
    for order in data["Orders"]:

        if order["order_id"] == order_id:
            data["Orders"].remove(order)
            return True
    return False

def count_orders(data):
    count = 0 
    for order in data["Orders"]:
        count+=1 
    return count

def count_orders_by_customer(data, customer_id):
    count = 0
    for order in data["Orders"]:
        if order["customer_id"] == customer_id:
            count +=1 
    return count


def update_order_status(data, order_id, new_status):
    order = find_order_by_id(data , order_id)
    if order is None:
        return False
    allowed_statuses = ["Pending" , "Preparing", "Completed", "Cancelled"]
    if new_status  not in allowed_statuses:
        return False
    order["status"] = new_status
    return True

def find_orders_by_status(data, status):
    results=[]
    for order in data["Orders"]:
       if order["status"] == status:
           results.append(order)
    return results

def count_orders_by_status(data, status):
    count = 0 
    for order in data["Orders"]:
       if order["status"] == status:
           count += 1 
    return count


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return quantity
            
def validate_order(data, product_id, quantity):
    product= get_valid_product(data , product_id)
    valid_quantity= validate_quantity(quantity)
    valid_order = {"product": product, "quantity": valid_quantity}
    return valid_order
