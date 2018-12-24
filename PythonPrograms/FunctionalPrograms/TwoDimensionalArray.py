from UtitlitiesMethod import Utility

try:
    rows = int(input("Enter number of rows \n"))
    coloumns = int(input("Enter number of coloumns \n"))
    Utility.twoDimensionalArray(rows,coloumns)
except Exception as e :
    print("Enter the numbers not characters")