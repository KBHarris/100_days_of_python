print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))

tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = float(input("How many people will split the bill? "))

split_amount = round(float(((total * (tip_percent / 100) + total) / people )), 2)

print(f"Each person should pay: ${split_amount}")