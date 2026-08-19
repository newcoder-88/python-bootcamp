def get_valid_age():  
    try:
        age = int(input("What's your age? "))
        if age < 0:
            return False
        else:
            return age
    except ValueError:
        return False
print(get_valid_age())