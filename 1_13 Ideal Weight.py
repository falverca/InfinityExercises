# Based on a person's height in cm, build a program that calculates their ideal weight using the formula: (72.7*height in meters) - 58

height_in_cm = float(input("How tall are you in cm? "))

height_in_m = height_in_cm / 100

ideal_weight = (72.7 * height_in_m) - 58

print(f"Your ideal weight is {ideal_weight}.")