# @Purpose To print the powers of 2
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018



from UtitlitiesMethod import Utility
try :
    number = int(input("Enter the Number \n"))
    if(number > 0 and number < 31) :
        Utility.printTable(number)
    else:
        print("Enter the valid input")
except Exception as e :
    print("Enter the digit not characters")