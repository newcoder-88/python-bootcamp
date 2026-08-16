students = [
    {"name": "Sarah", "age": 26},
    {"name": "Ali", "age": 24},
    {"name": "John", "age": 22},
    {"name": "Mike", "age": 28}
]


def update_student_age(students, name, new_age):
    for student in students:
        if student["name"] == name:
            student["age"] = new_age
#update_student_age(students, "Ali", 25)
#print(students)

def remove_student(students, name):
    for student in students:
        if student["name"] == name: 
            students.remove(student)
            return
#remove_student(students, "Ali")
#print(students)

def count_students(students):
    count= 0 
    for student in students: 
        count+= 1 
    return count
#print(count_students(students))

def add_student(students, name, age):
    newStudent ={"name": name , "age": age}
    students.append(newStudent)

#add_student(students, "Sarah", 27)
#print(students)

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None
#student = find_student(students, "David")
#print(student)

def find_students_by_age(students, age):
    result=[]
    for student in students: 
        if student["age"] == age:
            result.append(student["name"])
    return result
#result = find_students_by_age(students, 24)
#print(result)

def find_oldest_student(students):
    oldest = students[0]
    for student in students:
        if student["age"] > oldest["age"]:
            oldest  = student
    return oldest
#oldest = find_oldest_student(students)
#print(oldest)

def print_student(students, name):
    student = find_student(students, name)
    if student is None: 
        print("Student not found")
    else:
        print("Name:" , student["name"])
        print("Age:" , student["age"])

print_student(students, "David")
print_student(students, "Sarah")