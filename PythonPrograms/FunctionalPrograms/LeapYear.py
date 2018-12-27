# @Purpose To check weather the year is leap year or not
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility

try :
    year = int(input("Enter the Year \n"))
    Utility.leapYear(year)
except Exception as e :
    print("Enter the year in the form of numbers")