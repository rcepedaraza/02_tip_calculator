# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay $33.6
# Round the result to 2 decimal places
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

each_pay = round(((total_bill * (tip_percentage + 100) / 100) / total_people), 2)
print(f"Each person should pay: ${each_pay:.2f}")