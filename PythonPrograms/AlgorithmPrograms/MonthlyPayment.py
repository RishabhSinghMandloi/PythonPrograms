# @purpose
## to calculate the monthly payment which we have to give on the principal amount
## on the given rate of intrest and within the given time peroid


# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018

from UtitlitiesMethod import Utility

try:
    p = int(input("Enter principal amount:"))
    y = int(input("Enter years :"))
    r = int(input("Enter rate of Intrest:"))
    Utility.monthlyPayment(p,y,r)
except Exception as e :
    print("Enter the valid input")