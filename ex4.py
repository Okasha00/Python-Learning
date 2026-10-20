# Ask for marks (0-100) and print the grade: A (80+), B (70+), C (60+), D (50+), otherwise F.



marks=int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a number between 0 and 100.")

elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")   

elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")