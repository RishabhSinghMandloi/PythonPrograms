# @Purpose To calculate the minimum amount of notes by the vending machine
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility

try:
    notes = [1000,500,100,50,10,5,2,1]
    money = int(input("Enter the amount : "))
    Utility.vendingMachine(money ,  notes)
except Exception as e:
    print("Enter the valid input ")

