# Build a program that asks for two integers and one real number. Calculate and show:
# the product of the double of the first number with half of the second one.
# the sum of triple of the first number with the third number.
# the third number to the power of 3.

int1 = int(input("Insert an integer: "))
int2 = int(input("Insert another integer: "))
real3 = float(input("Insert a real number: "))

print(f"The product of the double of the first number with half of the second one is equal to {(int1 * 2) * (int2 / 2)}.")
print(f"The sum of triple of the first number with the third number is equal to {(int1 * 3) + real3}.")
print(f"The third number to the power of 3 is equal to {real3 ** 3}.")