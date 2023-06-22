'''
100 Days of Code

Day 3 - Treasure Island
'''
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("\n\nYou're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

match direction:  
    case 'right':
        decision = input("\nYou've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
        match decision:
            case 'wait':
                colour = input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
                match colour:
                    case 'red':
                        print("\nIt's a room full of fire. Game Over.")
                        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    case 'yellow':
                        print("\nYou enter a room of beasts. Game Over.")
                        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    case 'blue':
                        print("\nYou found the treasure! You Win!")
                    case default:
                        print("\nYou chose a door that doesn't exist. Game Over.")
                        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            case default:
                print("\nYou get attacked by an angry trout. Game Over.")  
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")      
    case default:
        print("\nYou fell into a hole. Game Over.")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
