expression = input("Math expression: ")
brackets = []

for char in expression:
    if char == "(":
        brackets.append("(")
    elif char == ")":
        if len(brackets) > 0:
            brackets.pop()
        else:
            brackets.append(")")

if len(brackets) != 0:
    print("Invalid expression!")
else:
    print("Valid expression!")
