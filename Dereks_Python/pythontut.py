#!/usr/bin/python3

# Ask the user to input 2 values and store them in variables num1 and num2 to allow maths calculation

# Longer way of doing it, not efficent 
# num1 = input('What is number 1? ')
# num2 = input ('What is number 2? ')
num1, num2 = input('What is the number: ').split()

# Conver the strings into regular numbers Integers

# long way - num1 = int(num1)
# long way - num2 = int(num2)
num1, num2 = int(num1), int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract values and store in varible known as difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print the results - different way using formats
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
# Print the results - different way using f-string
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")
print(f"{num1} % {num2} = {remainder}")