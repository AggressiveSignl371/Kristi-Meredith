#Tip calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_per_person = (total_bill*(tip/100))/people
bill_per_person = (total_bill/people) + tip_per_person
print(f"Each person should pay: ${bill_per_person}")