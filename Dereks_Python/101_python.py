#!/usr/bin/python3
# receive miles and convert to kilometers
# kilometers = miles * 1.60934

# Ask user for miles
miles = input("How many miles? ")

# Convert from str to float (to allow decimal places)
miles = float(miles)

# Calculation for conversion
kilometers = miles * 1.60934

# Print results of conversion
# f-string
print(f"{kilometers:.2f} kilometers is equal to {miles} miles.")
print(f"{miles} miles is equal to {kilometers} kilometers")
print(f"{miles} miles is equal to {kilometers:.2f} kilometers")
# format
print("{} miles equals {} kilometers".format(miles, kilometers))