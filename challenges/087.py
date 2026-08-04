matrix_size = 3
matrix = [
    [],
    [],
    [],
]

# Input matrix data
for line in range(matrix_size):
    for col in range(matrix_size):
        num = int(input(f"Line: {line} Col: {col} Value: "))
        matrix[line].append(num)

# Print matrix
for line in matrix:
    for col in line:
        print(col, end=" ")
    print()
print()

# Sum even numbers
sum_even = 0
for line in matrix:
    for col in line:
        if col % 2 == 0:
            sum_even += col

print(f"Even sum: {sum_even}")

# Sum third col values
sum = 0
for index in range(matrix_size):
    sum += matrix[index][2]

print(f"Sum of third col: {sum}")

# Print biggest value of second line
biggest = matrix[1][0]
for col in matrix[1]:
    biggest = max(col, biggest)

print(f"Biggest of second line: {biggest}")
