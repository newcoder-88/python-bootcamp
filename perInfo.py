student={"name": "sarah" , "age": 25 , "major": "information system"}

print(student["name"])
print(student["major"])

student["age"] = 26 
student["country"] = "saudi arabia"
print(student)

for key in student:
    print(key , ":" , student[key])



students = [
    {"name": "Sarah", "age": 26},
    {"name": "Ali", "age": 24},
    {"name": "John", "age": 22}
]

for student in students:
    print(student["name"] ,"-" ,student["age"])