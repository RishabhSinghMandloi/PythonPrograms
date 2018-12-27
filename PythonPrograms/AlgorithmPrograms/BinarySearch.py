from UtitlitiesMethod import Utility
li= list(input("enter number in your list \n").split(" "))
li=[int(x) for x in li]      #typecasting
li.sort()
print(li)
lowValue = 0
highValue = len(li)-1

element = int(input("Enter the element you want to search \n"))
result = Utility.binarySearch1(li, lowValue, highValue, element)
print(result)
