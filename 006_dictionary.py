person = {"name": "Jacson", "age": 25}

print(person["name"])
print(person["age"])

person["gender"] = "M"

print(person["gender"])

person["useless_prop"] = "69"

del person["useless_prop"]

print(person.values())
print(person.keys())
print(person.items())
