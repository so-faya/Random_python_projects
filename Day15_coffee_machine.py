MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 24,
}

should_continue = True

while should_continue:
#TODO 1: prompt "What would you like? (espresso/latte/cappuccino):"
    user_desire = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #TODO 2: a function to check user input for todo1
    if user_desire == "off":
        should_continue = False
        break
        # end the program

    if user_desire == "report":
        for content, amount in resources.items():
            print(f"{content}: {amount}")

    elif user_desire in MENU:
        user_choice = user_desire


    #TODO 3: A function to check if the there are enough resource for the picked drink
        def check_enough_resources(drink):
            resource_directory = MENU[drink]["ingredients"]

            for content, required_amount in resource_directory.items():
                available_amount = resources.get(content, 0)
                if available_amount < required_amount:
                    print("insufficient resources")
                    return False
            print("enough resources")
            return True

        # TODO 7: if TODO 6 is complete  minus the use resources from available reasources
        def update_resources(drink):
            for ingredient, amount in MENU[drink]["ingredients"].items():
                resources[ingredient] -= amount

        if check_enough_resources(user_choice):
            # TODO 4: Prompt "Insert coins" if the Todo 3 is enough
            print("Please insert coin:")
            penny = int(input("How many Pennies? "))
            nickel = int(input("How many Nickles? "))
            dime = int(input("How many Dimes? "))
            quarter = int(input("How many Quarters? "))

            #TODO 5: calculate the the coins according to the rules
            penny *= 0.01
            nickel *= 0.05
            dime *= 0.10
            quarter *= 0.25

            solution = penny + nickel + dime + quarter
            # print(solution)

            #TODO 6: Check if the coin is enough
            def check_enough_money(num, drink):
                if num == MENU[drink]["cost"]:
                    print(f"Here is your {drink}")
                    update_resources(user_choice)
                    return True
                elif num > MENU[drink]["cost"]:
                    num -= MENU[drink]["cost"]
                    print(f"Here is your drink and your change is {num}")
                    update_resources(user_choice)
                    return True
                else:
                    print(f"Not enough funds")
                    return False
            check_enough_money(solution, user_choice)

    else:
        print("Invalid choice, please select 'espresso', 'latte', 'cappuccino', or 'report'. ")
