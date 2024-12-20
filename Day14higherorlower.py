import random
import Day14art
import Day14game_data

# for the logo
print(Day14art.logo)

# function for the format
def competitor_format(account):
    account_name = account["name"]
    account_occpu = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_occpu} from {account_country}"



# for the second contestant
contestant_b= random.choice(Day14game_data.data)




score = 0
should_continue= True
while should_continue:
    contestant_a = contestant_b
    print(f"Compare A: {competitor_format(contestant_a)}")

    # the second logo
    print(Day14art.vs)

    contestant_b = random.choice(Day14game_data.data)
    print(f"Against B: {competitor_format(contestant_b)}")

    # user make a guess
    guessing= input("Who has more followers? Type 'A' or 'B':").lower()

    # function for compare
    def high_celeb():
        contestant_arate = contestant_a["follower_count"]
        contestant_brate = contestant_b["follower_count"]
        if contestant_arate > contestant_brate:
            return guessing == 'a'
        else:
            return guessing == 'b'

    # function if the user guess is correct
    right_guess = high_celeb()
    print(right_guess)
    if right_guess:
        score += 1
        print("\n"*20)
        # for the logo
        print(Day14art.logo)
        print(f"You're right! Current score {score}")
        # should_continue = True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False



