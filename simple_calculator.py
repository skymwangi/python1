#prompt the user for two numbers
numero1= float(input("Enter first number: "))
numero2= float(input("Enter second number: "))

#prompt user to enter operator
operator=input("Enter an operator (+,-,*,/):")
#perform calculation based on operators
if operator =="+":
    result = numero1+numero2
elif operator =="-":
    result = numero2-numero1
elif operator == "*":
    result = numero1*numero2
elif operator =="/":
    if numero2!= 0:
        result = numero1/numero2
    else:
        result = "Error, divisible by zero"
else:
    result = "Invalid operator"
print(f"The answer is {result}")