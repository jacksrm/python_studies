print("Type the 3 sides size of a triangle")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

triangle = a + b > c and b + c > a and c + a > b

if triangle:
    print("It is a triangle")
else:
    print("It isn't a triangle")
