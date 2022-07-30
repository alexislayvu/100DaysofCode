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


def drink_menu():
    """Displays the coffee menu."""
    print("----- COFFEE MENU -----")
    print("Espresso:    $1.50")
    print("Latte:       $2.50")
    print("Cappuccino:  $3.00")


def make_coffee(drink_name, drink_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def process_payment():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def sufficient_resources(drink_ingredients):
    """Returns True when an order can be made, False if ingredients are insufficient."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def transaction(money_received, drink_cost):
    """Returns True when the payment is accepted, False if money is insufficient."""
    global profit
    change = round(money_received - drink_cost, 2)
    # money_received = total
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif money_received > drink_cost:
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        profit += drink_cost
        return True


drink_menu()

machine_on = True
while machine_on:
    choice = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_payment()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Not a valid drink, try again.")
