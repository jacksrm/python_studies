names = []
heaviest = 0
lightest = 0

while True:
    name = input("Type a name ('q' to quit): ")
    if name == "q":
        break

    weight = input(f"{name}'s weight ('q' to quit): ")
    if weight == "q":
        break

    weight = float(weight)
    heaviest = max(heaviest, weight)

    if weight < lightest or lightest == 0:
        lightest = weight

    names.append([name, weight])

print(f"{len(names)} were registered")
print(f"The heaviest weight was {heaviest}, they were: ", end="")

for person in names:
    if person[1] == heaviest:
        print(f"[{person[0]}]", end=" ")

print()

print(f"The lightest weight was {lightest}, they were: ", end="")

for person in names:
    if person[1] == lightest:
        print(f"[{person[0]}]", end=" ")
print()
