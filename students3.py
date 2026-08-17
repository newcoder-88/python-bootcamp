students = [
    {"name": "Sarah", "age": 26},
    {"name": "Ali", "age": 24},
    {"name": "John", "age": 22},
    {"name": "Mike", "age": 28}
]

def add_student(students, name, age):
    if age < 0 : # if age is < 0
        return False
    valid_name = name.strip() # remove spaces 
    if valid_name == "" : # if string is null 
        return False
    new_student = {"name": valid_name , "age": age}
    students.append(new_student)
    return True
result = add_student(students, " sarah ", 28)
print(result)
print(students)