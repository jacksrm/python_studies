print("Type 3 numbers")
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if n1 > n2:
    bigger = n1
    lesser = n2
else:
    bigger = n2
    lesser = n1

if n3 > bigger:  # noqa: PLR1730
    bigger = n3

if n3 < lesser:  # noqa: PLR1730
    lesser = n3

print(f"Bigger: {bigger}")
print(f"Lesser: {lesser}")
