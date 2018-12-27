# @Purpose Here we find the count of Random Number to find the distnict coupans
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018

from UtitlitiesMethod import  Utility

try :
    inputNumber = input("Enter  distinct coupans : \n")
    list = [int(i) for i in str(inputNumber)]
    Utility.coupans(list)
except Exception as e:
    print("Plese Enter the digits not characters")