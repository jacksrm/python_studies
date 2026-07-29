tax_day = 60
tax_km = 0.15
print("Calculating car rent price")
day = int(input("Days rented: "))
km = int(input("Km run: "))
price = day * tax_day + km * tax_km
print(f"The total price is R${price:.2f}")
