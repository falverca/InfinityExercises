# Build a program that asks for your hourly rate and how many hours you worked throughout the month. It should calculate and show the total of your salary in a given month.

hourly_rate = float(input("What's your hourly rate: "))
worked_hours = float(input("How many hours did you work this month? "))

salary = hourly_rate * worked_hours

print(f"Your salary will be {salary}.")