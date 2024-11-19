import random
import Day12_art

def game_function():
    # computer generates number
    computer_generated_number = random.randint(1,100)

    # first info gathered
    print(Day12_art.logo)
    print("Welcome to the Number Guessing Game! \n"
          "I'm thinking of a number between 1 and 100. \n"
          f"Psst the answer is {computer_generated_number}")

    # Request for user difficulty type
    difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    easy_game = 10
    hard_game = 5

    # rules for the difficulty type
    def difficulty_type_rule(difficulty):
        if difficulty == "easy":
            return easy_game
        elif difficulty == "hard":
            return hard_game

    attempts = difficulty_type_rule(difficulty_type)
    # print(attempts)


    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")

        # user makes a guess
        user_guess = int(input("Make a guess: "))

        # compare the user guess with the generated number
        if user_guess < computer_generated_number:
            print("Too Low")
            # print(f"You have {attempts} attempts remaining to guess the number.")
        elif user_guess > computer_generated_number:
            print("Too High")
            # print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"Congratulation, You guess the right answer, {computer_generated_number}")
            break
        attempts -= 1

        if attempts == 0:
            break

game_function()

main_continue = True

while main_continue:
    going_again = input("Would you like to go again? 'yes' or 'no' ").lower()

    if going_again == "yes":
        print("\n"* 20)
        game_function()
    else:
        main_continue = False



    

