height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = round(weight / (height * height), 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are under weight")
else:
    if bmi < 25:
        print(f"Your BMI is {bmi} and you are normal weight")
    elif bmi < 30:
        print(f"Your BMI is {bmi} and you slightly overweight")
    elif bmi < 35:
        print(f"Your BMI is {bmi} and you are obese weight")
    elif bmi >= 35:
        print(f"Your BMI is {bmi} and you are clinically weight")