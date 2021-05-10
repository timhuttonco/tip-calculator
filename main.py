print("Welcome to the tip calculator")
# Start with bill total
bill_total = float(input("What was the total bill? £"))
# Get tip total
percent_tip = int(input("What percentage tip would you like to give?"))
# Number of people splitting
people = int(input("How many people to split the bill?"))
# Add tip amount (percent number divided by 100 and multiplied by the bill total) to the bill total
final_total = percent_tip / 100 * bill_total + bill_total
# Divide the total of the bill by number of people
bill_per_person = final_total / people
# Format string to two decimal places
final_amount = "{:.2f}".format(bill_per_person)
# Print final amount
print(f"Each person should pay £{final_amount}")