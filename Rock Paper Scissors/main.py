"""
Day 4 - Rock Paper Scissors Project

Alexis Lay Vu
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
pc_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)
if user_choice == 1:
    print(paper)
if user_choice == 2:
    print(scissors)

print("Computer chose:")
if pc_choice == 0:
    print(rock)
if pc_choice == 1:
    print(paper)
if pc_choice == 2:
    print(scissors)

if user_choice - pc_choice == 0:
    print("Draw!")
if user_choice == 0 and pc_choice == 1:
    print("You lose :(")
if user_choice == 0 and pc_choice == 2:
    print("You win! :)")
if user_choice == 1 and pc_choice == 0:
    print("You win! :)")
if user_choice == 1 and pc_choice == 2:
    print("You lose! :(")
if user_choice == 2 and pc_choice == 0:
    print("You lose! :(")
if user_choice == 2 and pc_choice == 1:
    print("You win! :)")

