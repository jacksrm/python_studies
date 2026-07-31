numbers = []

while True:
    n = input("Type a number('q' to quit): ")

    if n == "q":
        break

    n = int(n)
    if n in numbers:
        continue

    numbers.append(n)
numbers.sort()
print(*numbers, sep=", ")
