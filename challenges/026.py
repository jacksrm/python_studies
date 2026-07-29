phrase = input("Write a phrase: ")
term = "a"
a_count = phrase.count(term)
a_first = phrase.find(term)
a_last = phrase.rfind(term)

print(f'Searching the letter "{term}"')
print(f"How many: {a_count}")
print(f"First position: {a_first}")
print(f"Last position: {a_last}")
