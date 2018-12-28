# @Purpose To caluculate the temprature in celsius and farenite
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility

try:
    fahernite = float(input("Enter the temprature in Farhenite :"))
    celsius = float(input("Enter the temprature in celsius "))
    Utility.tempratureConversion(celsius,fahernite)
except Exception as e:
    print("Enter the valid input")