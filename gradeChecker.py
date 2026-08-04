grade = int(input("What's your grade: "))

if grade > 100 or grade < 1:
    print("Invalid grade.")
else: 
     if grade >= 90 :
        print("Grade: A")
     elif grade >= 80 :
        print("Grade: B")
     elif grade >= 70 :
        print("Grade: C")
     else:
        print("Grade: F")