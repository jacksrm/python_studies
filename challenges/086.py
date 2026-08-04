matrix = [
    [],
    [],
    [],
]

for line in range(3):
    for col in range(3):
        num = int(input(f"Line: {line} Col: {col} Value: "))
        matrix[line].append(num)

for line in range(3):
    for col in range(3):
        print(matrix[line][col], end=" ")
    print()
