#!/usr/bin/python3

# Different outputs based on age
# 1 - 12 - very important
# 13 - offical teenager
# 14, 15, 17 - No one cares, go away
# 16 - omg sweet 16
# 18 - yay i can drive
# 19 - 20, no one cares, lets go party
# 21 - omg i can vote
# 22 - 30 - its all fun and games
# 30 - welcome to adulthood
# 30 - 39 - adulting is not fun
# 40 - offically old
# 41 - 49 - no one cares, everthing is hard
# 50 - u actually made it this far
# 51 - 59 - everything hurts i want to retire
# 60 - really really old
# 65 - retire now please
# everything else is why ?

# Input age
# age = input("How old are you, be honest? ")
# age =int(age)

age = eval(input("How old are you, be honest? ")) # eval converts straight into interger

if 0 < age < 12:
    print(f"Omg you special little fruitcake, how cute are you at {age}")
elif age == 13:
    print(f"Your offically a Teen! Happy {age} Birthday")
elif age == 16:
    print("O.M.G Sweet Sixteen")
elif age in [14, 15, 17]:
    print(f"No one care about your {age}th birthday and you can't drink")
elif age in [19, 20]:
    print(f"{age} birthday great excuse for a party")
elif age == 21:
    print(f"{age}st! A Voting Adult")
elif 22 < age < 30:
    print(f"Its all fun and games at {age}")
elif age == 30:
    print(f"Welcome to adulthood at {age}")
elif 31 < age < 40:
    print(f"{age}! Responsibilities! Adulting is not fun")
elif age == 40:
    print(f"{age}! Offically Old")
elif 51 < age < 60:
    print(f"At {age}, everything hurts and i just want to retire and be grumpy")
elif age == 65:
    print(f"At {age}, you should be retired")
else:
    print(f"At {age}, no one cares, you don't care, just do something nice for yourself and move on")
