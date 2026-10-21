from products import find_product_by_id
from customers import find_customer_by_id, count_customers
from orders import count_orders_by_customer, count_orders_by_status, count_orders

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

def calculate_total_revenue(data):
    total_rev = 0 
    for order in data["Orders"]:
        if order["status"] == "Completed":
            total_rev += order["total"]
    return total_rev

def calculate_average_order_value(data):
    total_rev = calculate_total_revenue(data)
    total_orders = count_orders_by_status(data , "Completed")
    if total_orders == 0 :
        return 0 
    avg = total_rev / total_orders 
    return avg 

def find_top_customer(data):
    customer_summaries = get_all_customer_summaries(data)
    if len(customer_summaries) == 0 :
        return None
    top_spender = customer_summaries[0]
    for customer in customer_summaries:
        if customer["total_spent"] > top_spender["total_spent"]:
            top_spender = customer
    return top_spender

def find_top_product(data):
    product_sales = get_all_product_sales(data)
    if len(product_sales) == 0 : 
        return None
    top_product = product_sales[0]
    for product in product_sales:
        if product["revenue"] > top_product["revenue"]:
            top_product = product
    return top_product

def generate_shop_report(data):
    total_customer = count_customers(data)
    total_orders = count_orders(data)
    total_rev = calculate_total_revenue(data)
    avg_order_rev = calculate_average_order_value(data)
    top_customer = find_top_customer(data)
    top_product = find_top_product(data)
    report ={"total_customers": total_customer, "total_orders": total_orders, "total_revenue": total_rev, "average_order_value":avg_order_rev ,"top_customer":top_customer , "top_product": top_product}
    return report
