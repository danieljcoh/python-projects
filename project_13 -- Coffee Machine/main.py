from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO
# Report
# Check resources sufficient
# Process Coins
# Check Transaction successful
# Make Coffee


def main():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        desired_drink = input(f"{menu.get_items()} or report: ")
        if desired_drink == "report":
            coffee_maker.report()
            print()
            money_machine.report()
        elif desired_drink == "latte" or desired_drink == "espresso" or desired_drink == "cappuccino":
            item = menu.find_drink(desired_drink)
            can_make = coffee_maker.is_resource_sufficient(item)
            if can_make: 
                proceed = money_machine.make_payment(item.cost)
                if proceed:
                    coffee_maker.make_coffee(item)
        else:
            print("Sorry. We don't have that drink!")


    



if __name__ == "__main__":
    main()