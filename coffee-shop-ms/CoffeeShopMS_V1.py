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



