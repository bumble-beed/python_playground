#!/usr/bin/python3
# Build calculator
# Allow + - / * %

# Store user input of 2 numbers and operators
num1, operator, num2 = input("What is the number? ").split()

# Convert from str to float for decimal places
num1, num2 = float(num1), float(num2)
# if + - / * %, then output based on operator
# # f-string
if operator == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1*num2}")
elif operator == "/":
    print (f"{num1} / {num2} = {num1/num2}")
elif operator == "%":
    print (f"{num1} % {num2} = {num1%num2}")
else:
    print("Invalid input, Allowed + - * /%")

# format
if operator == "+":
    print("{} + {}) = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {}) = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {}) = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {num2}) = {}".format(num1, num2, num1/num2))
else:
    print("Invalid input, Only allowed + - * /")