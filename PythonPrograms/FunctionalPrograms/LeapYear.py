from UtitlitiesMethod import Utility

try :
    year = int(input("Enter the Year \n"))
    Utility.leapYear(year)
except Exception as e :
    print("Enter the year in the form of numbers")