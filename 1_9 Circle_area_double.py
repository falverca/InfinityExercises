# Build a program that asks for the radius of a circle (cm) and shows its area x 2. Pi = 3

radius = float(input("What's the radius of the circle in cm: "))
pi = 3

area = pi * (radius ** 2)

print(f"The doubled area of the circle is {area * 2}.")