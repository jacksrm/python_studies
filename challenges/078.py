numbers = []
while len(numbers) < 5:
    n = int(input("Type a number: "))
    numbers.append(n)

big = numbers[0]
big_i = []
small = numbers[0]
small_i = []

for index, num in enumerate(numbers):
    big = max(big, num)
    small = min(small, num)

for index, num in enumerate(numbers):
    if num != big and num != small:
        continue
    if num == big:
        big_i.append(index)
    else:
        small_i.append(index)


print(f"Biggest: {big} Position(s): {', '.join(map(str, big_i))}")
print(f"Smallest: {small} Position(s): {', '.join(map(str, small_i))}")
