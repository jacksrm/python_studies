distance = int(input("Travel distance(Km): "))
price = 0
tax_km = 0.5 if distance <= 200 else 0.45

price = distance * tax_km
print(f"Travel cost: R${price}")
