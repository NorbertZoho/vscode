# Life in Weeks

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Asking for current age in years

current_age = input("What is your  current age? ")

# Calculating current age in days

age_in_days = int(current_age)*365
age_in_weeks = int(current_age)*52
age_in_months = int(current_age)*12

days_left = (90*365) - (age_in_days)
weeks_left = (90*52) - (age_in_weeks)
months_left = (90*12) - (age_in_months)

print(f"You have  {days_left} days, {weeks_left} weeks, and {months_left} months left")

# Simpler solution: 
# age_left = 90 - current_age
# days_left = 365*age_left, etc...