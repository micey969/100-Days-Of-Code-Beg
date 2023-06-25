'''
100 Days of Code

Day 4 - Tip CalculatorRock Paper Scissors
'''
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

print("Welcome to Rock, Paper, Scissors")
choice = int(input("Please enter your choice. Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer = random.randint(0,2)

match choice:
    case 0: 
        if (computer == 0):
            print("Draw. You both chose:")
            print(rock)
        elif (computer == 1):
            print("Computer wins!!!")
            print(paper)
        else:
            print("You win!!! The computer chose")
            print(scissors)
    case 1: 
        if (computer == 1):
            print("Draw. You both chose:")
            print(paper)
        elif (computer == 2):
            print("Computer wins!!!")
            print(scissors)
        else:
            print("You win!!! The computer chose")
            print(rock)
    case 2:
        if (computer == 2):
            print("Draw. You both chose:")
            print(scissors)
        elif (computer == 0):
            print("Computer wins!!!")
            print(rock)
        else:
            print("You win!!! The computer chose")
            print(paper)
    case default:
        print("This is not a valid option. Sorry, you lose.")

print("Good game.")