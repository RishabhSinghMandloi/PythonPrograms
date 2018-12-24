from UtitlitiesMethod import Utility
try :
    number = int(input("Enter the Number \n"))
    if(number > 0 and number < 31) :
        Utility.printTable(number)
    else:
        print("Enter the valid input")
except Exception as e :
    print("Enter the digit not characters")