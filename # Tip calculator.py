# Tip calculator

print("Welcome to the tip calculator!")

# Asking the total bill
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would like to give? 10, 12 or 15%? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill*(1+tip_percentage/100)

pay = bill_with_tip / people

final_amount = round(pay, 2)
print(f'Each person should pay {final_amount} $')