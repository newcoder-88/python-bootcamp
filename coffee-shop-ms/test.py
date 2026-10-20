from customers import add_customer , find_customer_by_id , remove_customer , count_customers
data = {
    "customers": [
        {"customer_id": 1, "name": "Sarah", "email": "sarah@example.com"},
        {"customer_id": 2, "name": "Ali", "email": "ali@example.com"},
        {"customer_id": 3, "name": "Mona", "email": "mona@example.com"}
    ]
}

print(count_customers(data))
data["customers"] = []
print(count_customers(data))