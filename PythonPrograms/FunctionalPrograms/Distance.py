from UtitlitiesMethod import Utility
try:
    a = int(input("Enter your first coordinate \n"))
    b = int(input("Enter your second coordinate \n"))
    Utility.distanceCalculation(a,b)
except Exception as e :
    print("Invalid Input")
