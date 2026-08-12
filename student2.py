students = [
    {"name": "Sarah", "age": 26},
    {"name": "Ali", "age": 24},
    {"name": "John", "age": 22}
]


def update_student_age(students, name, new_age):
    for student in students:
        if student["name"] == name:
            student["age"] = new_age
#update_student_age(students, "Ali", 25)
print(students)

def remove_student(students, name):
    for student in students:
        if student["name"] == name: 
            students.remove(student)
            return
#remove_student(students, "Ali")
print(students)

def count_students(students):
    count= 0 
    for student in students: 
        count+= 1 
    return count
print(count_students(students))