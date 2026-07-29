salary = float(input("Type your salary: "))
raise_tax = 0.1 if salary > 1250 else 0.15
new_salary = salary * (1 + raise_tax)

print(f"New salary: R${new_salary:.2f}")
