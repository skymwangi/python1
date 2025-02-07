weight=float(input("Enter your weight in pounds: "))
height=float(input("Enter your height in inches: "))
BMI= (weight*703)/(height**2)
if BMI<18.5:
    result="underweight"
elif BMI>=18.5:
    result="normal weight"
elif BMI>=25:
    result="overweight"
elif BMI>=30:
    result="obese"
elif BMI>=35:
    result="extremely obese"
print(f"You are {result}")
print({BMI})