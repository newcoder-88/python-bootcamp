from products import add_product, find_product, find_product_by_id, update_product_price, remove_product
from customers import add_customer, find_customer_by_id, remove_customer, count_customers
from orders import calculate_item_total, create_order_item, create_order, calculate_order_total, find_order_by_id , find_orders_by_customer, remove_order, count_orders, count_orders_by_customer, update_order_status, find_orders_by_status , count_orders_by_status
from reports import calculate_product_quantity_sold, calculate_product_revenue, get_product_sales_summary, get_all_product_sales, calculate_customer_total, get_customer_summary, get_all_customer_summaries, calculate_total_revenue, calculate_average_order_value, find_top_customer, find_top_product, generate_shop_report
data={
    "Products":[],
    "order_items":[],
    "Orders":[], 
    "customers":[]
    }

# --------------Products--------------


#--------------Order_items--------------

#--------------Orders--------------

#--------------customers--------------


#--------------integrated --------------

#--------------testing--------------
          
add_product(data, 1, "Matcha", 25)   # True
add_product(data, 2, "Latte", 18)    # True
add_product(data, 3, "MATCHA", 20)   # False
add_product(data, 4, "   ", 20)     # False
update_product_price(data, "matcha", 30)

#print(calculate_item_total(data, 1, 3))

#print(count_orders(data))
#print(calculate_order_total(data))

#---------add customer---------
add_customer(data, 1, "sarah", "test@email.com")
create_order_item(data, 1, 2)
create_order_item(data, 2, 1)

create_order(1, 1, data)
#---------add customer---------
add_customer(data, 2, "maya", "test@email.com")
create_order_item(data, 1, 3)
create_order(2, 2, data)

#print(count_customers(data))
#print(find_orders_by_customer(data, 1)_



#print(find_orders_by_customer(data, 1))
#print(count_orders_by_customer(data, 1))


#print("total quan= " , calculate_product_quantity_sold(data, 1))
#print("total rev= " , calculate_product_revenue(data, 1))

update_order_status(data, 1, "Completed")
#print(count_orders_by_status(data, "Completed"))



