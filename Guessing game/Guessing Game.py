import random


number_to_guess = random.randint(1, 10)

print("Guess the number between 1 and 10:")

while True:
    guess = int(input("Your guess: "))

    if guess == number_to_guess:
        print("You guessed right!")
        break
    else:
        print("Try again!")






