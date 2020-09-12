# Write a program that asks the user how many feet and how many inches tall they are.
# Compute and print that equivalent number in centimeters
# 1 foot = 12 inches
# 1 inch = 2.54 cm

feet = int(input("How tall are you in feet? "))
inches = int(input("How tall are you in inches? "))

ft_in_inches = (feet * 12) + inches
inches_in_cm = (ft_in_inches * 2.54)

print("You are " + str(inches_in_cm) + " tall in cm.")