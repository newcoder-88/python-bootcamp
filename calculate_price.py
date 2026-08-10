def calculate_price(price , quantity , tax = 0):
    return price * quantity + tax

total1 = calculate_price(10, 3)
total2 = calculate_price(10, 3, 5)
print(total1)
print(total2)

def calculate_discount(price , discount=0):
    return price - discount 
Final_price = calculate_discount(100,20)
print(Final_price)
Final_price2 = calculate_discount(100)
print(Final_price2)

def check_grade(grade):
    if (grade >= 90 ):
        return "A"
    elif (grade >= 80):
        return "B"
    elif(grade >= 70):
        return "C"
    else:
        return "F"
    

print(check_grade(72))