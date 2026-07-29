limit = 80
tax_per_km = 7.0
speed = int(input("Current Speed: "))
if speed > limit:
    over_speed = speed - limit
    print("You've been charged!")
    print(f"{over_speed}Km/h over the Limit of {limit}Km/h")
    print(f"You have to pay R${tax_per_km * over_speed}")
