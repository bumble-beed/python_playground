#!/usr/bin/python3

# Different outputs based on age

# Input age and store
age = eval(input("How old are you? "))
# and if both are true it returns true
# or if either condition is true, then true
# not : convert a true condition to false

# If age >= 1 and age <= 18 This is a important birthday
if (age >= 1) and (age <= 18):
    print("This is an important Birthday")
# If age is 21, 30, 50 IMPORTANT 
elif (age == 21) or (age == 30):
    print("This is a VERY important Birthday")
# Check if age is less than 65, and then convert true to false and vice versa
elif not (age < 65):
    print("This is an important Birthday")
# Rest not important
else:
    print("Sorry Not Important")