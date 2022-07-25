from menu_data import resources
from menu_data import MENU

water = 0
milk = 0
coffee = 0
money = 0.0

order = input("What would you life? (espresso/latte/cappuccino): ").lower()
if order == "report":
    for supplies in resources:
        print(f"{supplies.title()}: {resources[supplies]}")