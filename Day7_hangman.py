import random
from Day7_hangman_words import word_list
import Day7_hangman_art


lives = 6

# used imported logo, used random to pick a random number from the random word, generated a place holder
print (Day7_hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    #  Update for the user on how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""
    if guess in correct_letters:
        print(f"this letter {guess} already exits")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # if statement if you guessed the wrong word

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            #  print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE. IT WAS {chosen_word.upper()}**********************")

    # if statement when you answer all the question
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # print the stages List from the file hangman_art.py

    print(Day7_hangman_art.stages[lives])
