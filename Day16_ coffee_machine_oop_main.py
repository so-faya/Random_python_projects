from Day16_coffee_menu_oop import Menu, MenuItem
from Day16_coffee_maker_oop import CoffeeMaker
from money_machine import MoneyMachine

display_menu = Menu()
# menu_item= MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options= display_menu.get_items()
    choice = input(f"what drink would you like to order {options}: ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if display_menu.find_drink(choice):
            drink = display_menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


