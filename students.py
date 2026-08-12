students = [
    {"name": "Sarah", "age": 26},
    {"name": "Ali", "age": 24},
    {"name": "John", "age": 22}
]


def find_student_age(students , name):
    for student in students:
        if name == student["name"]:
            return student["age"]
        
print(find_student_age(students , "Ali"))

def find_students_above_age(students, age):
    result = []
    for student in students: 
        if student["age"] > age : 
            result.append(student["name"])
    return result
print(find_students_above_age(students, 23))

def find_average_age(students):
    count = 0 
    stuages = 0
    for student in students: 
        count += 1 
        stuages += student["age"]
    avg = stuages / count
    return avg
print(find_average_age(students))