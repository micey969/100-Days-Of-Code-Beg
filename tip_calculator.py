'''
100 Days of Code

Day 2 - Tip Calculator
'''

print("Welcome to the tip calculator.")
bill =  float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you lik to give? 10, 12, or 15? "))

payment = (bill/people) + ((bill/people)*tip/100)

print("Each person should pay: $%.2f" %payment)