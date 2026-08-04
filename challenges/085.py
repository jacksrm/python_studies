numbers = [[], []]

for i in range(1, 8):
    n = int(input(f"{i}° number: "))

    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

print(f"Even: {sorted(numbers[0])}")
print(f"Odd: {sorted(numbers[1])}")
