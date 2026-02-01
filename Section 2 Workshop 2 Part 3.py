user_grade = int(input("Please enter your grade from 0 to 100: "))


if user_grade < 0 or user_grade > 100:
    print("Error: Grade must be between 0 and 100.")
elif user_grade >= 90 or user_grade == 100:
    print("You got an: A")
elif user_grade >= 80 or user_grade <= 89:
    print("You got a: B")
elif user_grade >= 70 or user_grade <= 79:
    print("You got a: C")
elif user_grade >= 60 or user_grade <= 69:
    print("You got a: D")
else:
    print("You got an: F")