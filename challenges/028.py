from random import randint

rand_num = randint(0, 5)
num = int(input("type a number between 0 and 5: "))
if num == rand_num:
    print("Correct!! Congrats!")
else:
    print("Wrong!! Too Bad!")
