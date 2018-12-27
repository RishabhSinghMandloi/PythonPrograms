# @Purpose To find the percentage of number of  wins and loss
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018



from UtitlitiesMethod import  Utility

name = input("Enter your name gambler\n")
stack = int(input("Enter the amount you have in your stack\n"))
target = int(input("Enter your target\n"))
bet = int(input("Enter your fixed bet amount\n"))
print("Hello ",name)
print("Your Initial data is ")
print("Your Stack is : ",stack)
print("Your target is : ",target)
print("Fixed Bet Amount: ",bet)

wins = Utility.gambler(stack,target,bet)
print("Total no of wins ",wins)
