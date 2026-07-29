text = "Coding in python is easy"

# slicing
# text[start:end<exclusively>:step]
print(f'"{text[8]}"')
print(f'"{text[8:13]}"')
print(f'"{text[8:24:2]}"')
print(f'"{text[:10]}"')
print(f'"{text[10:]}"')
print(f'"{text[8::3]}"')

# string size
print(len(text))
# counting substring
print(text.count("i"))
# count substring with slicing
print(text.count("i", 0, 13))
# finding text
print(text.find("py"))
# check substring with "in"
print("python" in text)

# Strings are immutable
# replace elements (returns a new string)
print(f'"{text.replace("python", "android")}"')

print(f'"{text.upper()}"')
print(f'"{text.lower()}"')
print(f'"{text.capitalize()}"')
print(f'"{text.title()}"')

text_spaces = "    Coding in python is easy   "
## trim spaces
print(f'"{text_spaces}"')
print(f'"{text_spaces.strip()}"')

# split string
# default is spaces
print(text.split())
print(text.split("i"))

# join a separator into a string
# works best if its a collection of strings
print("-".join(text))  # will put a separator after each character
text_split = text.split()
print("-".join(text_split))
