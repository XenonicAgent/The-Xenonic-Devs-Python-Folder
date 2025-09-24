height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height / 100 )**2
print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You're underweight")
elif BMI <= 24.9:
    print("You're healthy")
elif BMI <= 29.9:
    print("You're overweight")
elif BMI <= 34.9:
    print("You're severely overweight")
elif BMI <= 39.9:
    print("You're obese")
else:
    print("You're severely obese")