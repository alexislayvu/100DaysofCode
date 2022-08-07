from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_choice = input("What would you like? (latte/espresso/cappuccino): ").lower()

machine_on = True
while machine_on:
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "latte" or user_choice == "espresso" or user_choice == "cappuccino":
        if coffee_maker.is_resource_sufficient(user_choice):
            payment = money_machine.process_coins()
            money_machine.make_payment(payment)
        pass
    else:
        print("That is not a valid option. Try again!")

