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


def find_product_by_id(data, product_id):
    for product in data["Products"]:
        if product["id"] == product_id:
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

def get_valid_product(data, product_id):
    product = find_product_by_id(data, product_id)

    if product is None:
        raise ValueError("product not found")

    return product