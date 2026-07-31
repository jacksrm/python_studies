numbers = []
even = []
odd = []

while True:
    n = input("Type a number('q' to quit): ")

    if n == "q":
        break

    n = int(n)
    numbers.append(n)

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Numbers: {numbers}")
print(f"Even: {even}")
print(f"Odd: {odd}")
