from UtitlitiesMethod import Utility

# ls = [45,1 ,2 , 3 ,4,5,]

user_in = input("Enter the number seprated  by space: ")
lst = user_in.split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(Utility.mergeSort(lst))
