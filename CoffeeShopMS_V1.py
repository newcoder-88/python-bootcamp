data={
    "Products":[],
    "order_items":[],
    "Orders":[], 
    "customers":[]
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
  


def find_product(data, name):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower() == valid_name:
            return product
    return None


def update_product_price(data, name, new_price):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower() == valid_name:
            if new_price > 0:
                product["price"] = new_price
                return True
            return False
    return False



def remove_product(data, name):
    valid_name = name.strip().lower()
    for product in data["Products"]:
        if product["name"].lower()== valid_name:
            data["Products"].remove(product)
            return True
    return False


def find_product_by_id(data, product_id):
    for product in data["Products"]:
        if product["id"] == product_id:
            return product
    return None


#--------------Order_items--------------
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
    if quantity <= 0 :
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




#--------------Orders--------------
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

    new_order= {"order_id": order_id ,"customer_id": customer_id , "customer": customer["name"] , "items": order_items_copy ,"total": order_total }
    data["Orders"].append(new_order)
    data["order_items"]=[]
    return new_order




def find_order_by_id(data, order_id):
    for order in data["Orders"]:
        if order["order_id"] == order_id:
            return order
    return None
order = find_order_by_id(data, 1)

def find_orders_by_customer(data, customer_id):
    result=[]
    for order in data["Orders"]:
        if order["customer_id"] == customer_id:
            result.append(order)
    return result


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
def count_orders_by_customer(data, customer_id):
    count = 0
    for order in data["Orders"]:
        if order["customer_id"] == customer_id:
            count +=1 
    return count

def calculate_product_quantity_sold(data, product_id):
    productExist = find_product_by_id(data , product_id)
    if productExist is None:
        return None
    total_quantity = 0 
    for order in data["Orders"]:
        for item in order["items"]:
            if item["product_id"] == product_id:
                total_quantity += item["quantity"]
    return total_quantity

def calculate_product_revenue(data, product_id):
    productExist = find_product_by_id(data , product_id)
    if productExist is None:
        return None
    total_revenue = 0
    for order in data["Orders"]:
        for item in order["items"]:
            if item["product_id"] == product_id:
                total_revenue += item["total"]
    return total_revenue

def get_product_sales_summary(data, product_id):
    product = find_product_by_id(data , product_id)
    if product is None:
        return None
    total_quantity = calculate_product_quantity_sold(data , product_id)
    total_revenue = calculate_product_revenue(data , product_id)
    sale_summary = {"product_id": product["id"],"name": product["name"], "quantity_sold": total_quantity , "revenue": total_revenue}
    return sale_summary

def get_all_product_sales(data):
    products_summary = []
    for product in data["Products"]:
        product_summary = get_product_sales_summary(data, product["id"])
        products_summary.append(product_summary)
    return products_summary

#--------------customers--------------
def add_customer(data, customer_id, name, email):
    if customer_id <= 0:
        return False
    normalized_name = name.strip() 
    normalized_email = email.strip()
    if normalized_name == "":
        return False
    if normalized_email =="":
        return False
    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            return False
    new_customer = { "customer_id": customer_id , "name": normalized_name.title() , "email": normalized_email}
    data["customers"].append(new_customer)
    return True
        

def find_customer_by_id(data, customer_id):
    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
             return customer
    return None


def remove_customer(data, customer_id):
    customer = find_customer_by_id(data , customer_id)
    if customer is not None:
        data["customers"].remove(customer)
        return True
    return False


def count_customers(data):
    count= 0 
    for customer in data["customers"]:
        count += 1
    return count

def calculate_customer_total(data, customer_id):
    customer = find_customer_by_id(data , customer_id)
    if customer is None:
        return None
    total = 0 
    for order in data["Orders"] :
        if order["customer_id"] == customer_id:
            total += order["total"] 
    return total

def get_customer_summary(data, customer_id):
    customer = find_customer_by_id(data , customer_id)
    if customer is None:
        return None
    total_spent = calculate_customer_total(data , customer_id)
    order_count = count_orders_by_customer(data , customer_id)
    summary={"customer_id": customer["customer_id"] , "name": customer["name"], "order_count":order_count , "total_spent": total_spent}
    return summary

def get_all_customer_summaries(data):
    customers_summary = []
    for customer in data["customers"]:
       customer_summary= get_customer_summary(data , customer["customer_id"])
       customers_summary.append(customer_summary)
    return customers_summary

#--------------testing--------------
          
add_product(data, 1, "Matcha", 25)   # True
add_product(data, 2, "Latte", 18)    # True
add_product(data, 3, "MATCHA", 20)   # False
add_product(data, 4, "   ", 20)     # False
update_product_price(data, "matcha", 30)

#print(calculate_item_total(data, 1, 3))

#print(count_orders(data))
#print(calculate_order_total(data))

#-----------customer-----------
add_customer(data, 1, "sarah", "test@email.com")
create_order_item(data, 1, 2)
create_order_item(data, 2, 1)

create_order(1, 1, data)
#-----------customer-----------
add_customer(data, 2, "maya", "test@email.com")
create_order_item(data, 1, 3)
create_order(2, 2, data)

#print(count_customers(data))
#print(find_orders_by_customer(data, 1)_
print(data["Orders"])


#print(find_orders_by_customer(data, 1))
print(count_orders_by_customer(data, 1))


print("total quan= " , calculate_product_quantity_sold(data, 1))
print("total rev= " , calculate_product_revenue(data, 1))

print(get_product_sales_summary(data, 1))
print(get_all_product_sales(data))