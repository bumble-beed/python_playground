#!/usr/bin/python3

# If age is 5 go to Kindy
# Ages 6 -17 to Year 1 - 12
# if age > 17, go to college
# Try to complete program with less than 10 lines

age = int(input('How old are you? '))

if age < 5:
    print("You are too young for school")
elif age == 5:
    print(f'You go to Kinder at age {age}')
elif 6 < age < 17:
    year = age - 5
    print("Go to Year {}" . format(year)) # Old methiod using format
    print(f'At age {age} you would be in Year {year}') # using f-string
    print('Go to Year %d' % year) # % formatting (old school)
    print("Go to Year " + str(year)) # concat - simplest but not good for number
elif 17 <= age <= 24:
    print(f'Most people are either in University, Trade School and a PolyTech at age {age}')
else:
    print(f'Welcome to Adulting, Job and Responsibilities at {age}')