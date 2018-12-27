
# @Purpose To find the triplet which gives the sum of zero
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018





from UtitlitiesMethod import Utility
from array import *

arr = array('i',[])
length = int(input("Enter the size of Array \n"))
for i  in range(length):
    x=int(input("Enter the  Element :"))
    arr.append(x)
print(arr)
print()
Utility.findTriplet(arr)