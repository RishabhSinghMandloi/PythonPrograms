# @Purpose To find the Distance of cooridinates from the Origin
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility
try:
    a = int(input("Enter your first coordinate \n"))
    b = int(input("Enter your second coordinate \n"))
    Utility.distanceCalculation(a,b)
except Exception as e :
    print("Invalid Input")
