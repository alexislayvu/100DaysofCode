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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    """Returns True when an order can be made and deducts the required ingredients from the resources."""

    # if order == "latte" or order == "cappuccino":
    #     order_water = MENU[order]["ingredients"]["water"]
    #     order_milk = MENU[order]["ingredients"]["milk"]
    #     order_coffee = MENU[order]["ingredients"]["coffee"]
    #
    #     if order_water > resources["water"]:
    #         print("Sorry, there is not enough water.")
    #     elif order_milk > resources["milk"]:
    #         print("Sorry, there is not enough milk.")
    #     elif order_coffee > resources["coffee"]:
    #         print("Sorry, there is not enough coffee.")
    #     else:
    #         resources["water"] -= order_water
    #         resources["milk"] -= order_milk
    #         resources["coffee"] -= order_coffee
    #         return True
    #
    # elif order == "espresso":
    #     order_water = MENU[order]["ingredients"]["water"]
    #     order_coffee = MENU[order]["ingredients"]["coffee"]
    #
    #     if order_water > resources["water"]:
    #         print("Sorry, there is not enough water.")
    #     elif order_coffee > resources["coffee"]:
    #         print("Sorry, there is not enough coffee.")
    #     else:
    #         resources["water"] -= order_water
    #         resources["coffee"] -= order_coffee
    #         return True


def drink_menu():
    """Displays the coffee menu."""
    print("----- COFFEE MENU -----")
    print("Espresso:    $1.50")
    print("Latte:       $2.50")
    print("Cappuccino:  $3.00")


def print_report():
    """Prints a report of the supplies."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_payment(order):
    """"""
    # Get the cost of the order
    order_cost = MENU[order]["cost"]

    # Ask the user to insert the coins
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    # Calculate the leftover change
    change = round(total - order_cost, 2)

    if total < order_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return 0
    elif total > order_cost:
        print(f"Here is ${change} in change.")
        print(f"Here is your {order}. Enjoy!")
        return order_cost
    else:
        print(f"Here is your {order}. Enjoy!")
        return order_cost


drink_menu()

machine_on = True
while machine_on:
    choice = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            profit += process_payment(choice)
    else:
        print("Not a valid drink, try again.")
