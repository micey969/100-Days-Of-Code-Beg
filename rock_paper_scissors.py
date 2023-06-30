'''
100 Days of Code

Day 4 - Rock Paper Scissors
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
game_choice = [rock, paper, scissors]

print("You chose:")
print(game_choice[choice])

computer = random.randint(0,2)
print("\n\nComputer chose:")
print(game_choice[computer])

match choice:
    case 0: 
        if (computer == 0):
            print("Draw.")
        elif (computer == 1):
            print("Computer wins!!!")
        else:
            print("You win!!!")
    case 1: 
        if (computer == 1):
            print("Draw.")
        elif (computer == 2):
            print("Computer wins!!!")
        else:
            print("You win!!!")
    case 2:
        if (computer == 2):
            print("Draw.")
        elif (computer == 0):
            print("Computer wins!!!")
        else:
            print("You win!!!")
    case default:
        print("This is not a valid option. Sorry, you lose.")

print("Good game.")