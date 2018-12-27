# @Purpose To find the roots of the quadratic eqaution
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018



from UtitlitiesMethod import Utility

try:
    a = int(input("Enter the value of a \n"))
    b = int(input("Enter the value of b \n"))
    c = int(input("Enter the value of c \n"))
    Utility.quadraticFunctions(a,b,c)
except Exception as e:
    print("Enter a number not characters ")

