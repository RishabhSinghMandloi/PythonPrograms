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