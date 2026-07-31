numbers = []

while True:
    n = input("Type a number('q' to quit): ")

    if n == "q":
        break

    n = int(n)
    numbers.append(n)

numbers.sort()
print(f"Numbers typed: {len(numbers)}")
print(f"List: {numbers[::-1]}")
print(f"5 is present: {5 in numbers}")
