name = input("Write your full name: ")
words = len(name.split())
first = name.split()[0]
last = name.split()[words - 1]
print(f"First name: {first}")
print(f"Last name: {last}")
