from UtitlitiesMethod import  Utility

try :
    inputNumber = input("Enter  distinct coupans : \n")
    list = [int(i) for i in str(inputNumber)]
    Utility.coupans(list)
except Exception as e:
    print("Plese Enter the digits not characters")