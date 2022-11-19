"""
Day 2 - Tip Calculator
May 9, 2022
"""

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? ")
total_people = input("How many people to split the bill? ")

# Typecast the data types from str --> float
new_total_bill = float(total_bill)
new_total_people = float(total_people)
new_percentage = float(percentage)

# Calculate the tip percentage
tip_percentage = new_percentage / 100

# Split the bill
bill_split = new_total_bill / new_total_people

# Calculate payment per person
tip = bill_split * tip_percentage
payment = round(bill_split + tip, 2)

print(f"Each person should pay: ${payment}")
