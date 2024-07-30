User_height=float(input("Enter your  height in CM:"))
User_weight=float(input("Enter your weight in KG:"))
The_BMI=User_weight/(User_height/100)**2
print("Your Body Mass Index(BMI) is:",The_BMI)
if The_BMI<=18.5:
    print("You are Underweight")
elif The_BMI<=24.9:
    print("You are healthy!")
elif The_BMI<=29.9:
    print("You are Overweight")
else:
    print("You are Obese")

