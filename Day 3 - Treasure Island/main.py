"""
Day 3 - Treasure Island
May 18, 2022
"""

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

left_or_right = input("""You're at a crossroad, where do you want to go? Type "left" or "right". """)

if left_or_right.lower() == 'left':
    swim_or_wait = input(
        """You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. """)

    if swim_or_wait.lower() == 'wait':
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")

        if door.lower() == 'red':
            print("You were burned by fire. Game over.")
        elif door.lower() == 'blue':
            print("You were eaten by beasts. Game over.")
        elif door.lower() == 'yellow':
            print("You win!")
        else:
            print("Game over.")
    else:
        print("You were attacked by a trout. Game over.")
else:
    print("You just fell into a hole. Game over.")
