salary = float(input("Old salary: $"))
raise_amount = 0.15
new_salary = salary * (1 + raise_amount)
print(f"Raise: {raise_amount * 100}%")
print(f"New Salary: ${new_salary:,.2f}")
