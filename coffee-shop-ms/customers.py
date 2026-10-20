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