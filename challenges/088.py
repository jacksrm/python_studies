from random import randint

guesses = []
games_qtt = int(input("Quantity of games: "))
numbers_qtt = 6
min_game_value = 1
max_game_value = 60

# Generating games
for _ in range(games_qtt):
    guess = []
    for _ in range(numbers_qtt):
        generated = False
        number = 0
        while not generated:
            number = randint(min_game_value, max_game_value)
            if number not in guess:
                break
        guess.append(number)

    guesses.append(guess)

for i, guess in enumerate(guesses):
    print(
        f"Game N° {i + 1:0{len(str(len(guesses)))}}: [ {', '.join(f'{n:02}' for n in guess)}]"
    )
