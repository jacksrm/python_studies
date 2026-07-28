price = float(input("Product price: "))
discount_amount = 0.05
new_price = price * (1 - discount_amount)
print(f"Discount: {int(discount_amount * 100)}%")
print(f"New price: {new_price}")
