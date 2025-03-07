from datetime import datetime

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
current_date = datetime.now()

# Calculate age
age_years = current_date.year - birth_date.year
age_months = current_date.month - birth_date.month
age_days = current_date.day - birth_date.day

# Adjust for negative values
if age_days < 0:
    age_months -= 1
    age_days += (current_date.replace(month=current_date.month - 1, day=1) - current_date.replace(month=current_date.month - 2, day=1)).days

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"Exact age: {age_years} years, {age_months} months, and {age_days} days")