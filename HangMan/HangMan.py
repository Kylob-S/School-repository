import random
                     #Fruits to guess from
fruits = ['apple', 'banana', 'pear', 'kiwi', 'pineapple', 'strawberry', 'grapefruit',
          'orange', 'mango', 'cherry', 'blueberry', 'watermelon', 'peach', 'plum',
          'apricot', 'fig', 'blackberry', 'papaya', 'lemon', 'lime', 'pomegranate']
Secret_word = random.choice(fruits) #grabs a random fruit from "fruits"
guesses_left = len(Secret_word) + 2 #amount of guesses allowed before loss
guessed_letters = [] #Blank list you fill with letters you guess; you can't guess the same letters.

display_word = ['_'] * len(Secret_word) #Creates the underscores for the secret word

print("Welcome to HangMan!\nTry your luck...Guess the word!")#introduction

while guesses_left > 0:
    print(f"Current word: {' '.join(display_word)}")
    response = input(f"Guess a letter or the whole word. You have {guesses_left} guesses left: ").lower()
    if not response.isalpha():#checks a string to make sure it only contains alphabetical characters.
        print("Invalid input. Please enter a letter or the whole word (no numbers or symbols).")
        continue

    if response == Secret_word: #When won. This tells you you've guessed the word.
        print(f"Congratulations! You guessed the word '{Secret_word}'!")
        break
        #limits letters allowed to be guessed to one letter at a time
    elif len(response) == 1:
        if response in guessed_letters:
            print("You already guessed that letter.")

        elif response in Secret_word:#stores the users response if guessed correctly
            guessed_letters.append(response)

            #Fills in the blank spaces with the correct letters; After guessed.
            for i in range(len(Secret_word)):
                if Secret_word[i] == response:
                    display_word[i] = Secret_word[i]
            print(f"Good guess! '{response}' is in the word.")

        else:
            guessed_letters.append(response)
            guesses_left -= 1 #removes the amount of guesses you have left by 1
            print(f"Incorrect. '{response}' is not in the word.")
    else:
        print("Invalid input. Please guess a letter or the whole word.") #if anything but one letter is input as a response

        if "_" not in display_word:  # Check if all letters have been guessed
            print(f"Congratulations! You guessed the word '{Secret_word}'!")
            break

    if guesses_left == 0:#response to losing
        print(f"Sorry, you lose :( The correct word was '{Secret_word}'.")
