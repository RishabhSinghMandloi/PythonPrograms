from UtitlitiesMethod import Utility

number = int(input("Enter the range \n"))
for x in range(2,number,1):
    rs = Utility.checkPrime(x)
    if(rs):
     Utility.isPalindrome(x)
    print(x)




