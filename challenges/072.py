n_in_words = (
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
    "Twenty",
)
while True:
    n = int(input("Type a number between 0 and 20: "))
    if n < 0 or n > 20:
        print("Number out of bounds! Try again.")
    else:
        print(n_in_words[n])
        break
