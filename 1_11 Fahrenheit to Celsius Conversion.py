# Build a program that asks for a temperature in Fahrenheit and converts it to Celsius. Formula: C = 5 * ((F-32) / 9).

temp_fahrenheit = float(input("Fahrenheit to convert: "))

temp_celsius = 5 * ((temp_fahrenheit - 32) / 9)

print(f"{temp_fahrenheit} °F is equivalent to {temp_celsius} °C.")