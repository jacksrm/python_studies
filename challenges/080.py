numbers = []

last = None
insertion = None
for _ in range(5):
    n = int(input("Insert a number: "))

    position = 0
    while position < len(numbers) and numbers[position] < n:
        position += 1

    if len(numbers) == 0 or position == len(numbers) - 1 and numbers[position] < n:
        print("Added at list's end")
    else:
        print(f"Added at potion: {position}")

    numbers.insert(position, n)

print(numbers)
