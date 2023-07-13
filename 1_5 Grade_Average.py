# Build a program that asks for 4 bimonthly grades and shows the GPA

g1 = float(input("Insert the first grade: "))
g2 = float(input("Insert the second grade: "))
g3 = float(input("Insert the third grade: "))
g4 = float(input("Insert the forth grade: "))

gpa = (g1 + g2 + g3 + g4)/4

print(f"The GPA is {gpa}.")