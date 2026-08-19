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
    normalized_name = valid_name.lower()
    
    if valid_name == "" : # if string is null 
        return False
    for student in students: # if student exists
        if student["name"].lower() == normalized_name: 
            return False
    new_student = {"name": normalized_name.title() , "age": age}
    students.append(new_student)
    return True
#result = add_student(students, "  aLioN  ", 30)
#print(result)
#print(students)

def find_students_above_age(students, age):
    result= [] 
    for student in students:
        if student["age"] > age :
            result.append(student)
    return result
#result = find_students_above_age(students, 25)
#print(result)

def find_students(students, age, name):
    result = [] 
    for student in students:
        if student["age"] > age and student["name"] == name:
            result.append(student)
            # return student ##if only one student 
    return result
#result = find_students(students, 20, "Sarah")
#print(result)

def find_students_between_ages(students, min_age, max_age):
    result =[]
    for student in students:
        if student["age"] >= min_age and student["age"]<= max_age:
            result.append(student)
    return result
print(find_students_between_ages(students, 24, 28))
