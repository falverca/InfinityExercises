# Build a program that asks for the radius of a circle (cm) and calculates and shows its area. Pi = 3

radius = float(input("What's the radius in cm: "))
pi = 3

area = pi * (radius ** 2)

print(f"The area is {area}.")