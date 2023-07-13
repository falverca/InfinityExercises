# Build a program that reads the price of a product and shows its price with 5% off.

full_price = float(input("What's the price of the product? "))

off_5 = full_price * 0.95

print(f"The product costing R$ {full_price} will cost R$ {off_5} with 5% off.")