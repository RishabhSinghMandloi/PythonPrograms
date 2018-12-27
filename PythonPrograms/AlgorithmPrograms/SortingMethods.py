# @Purpose All the sorting methods are present
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018

from UtitlitiesMethod import Utility
try:

    print(" Press 1 for BinarySearch method of Integer")
    print("Press 2  for BinarySearch method of String")
    print("Press 3 for InsertionSort method of Integer")
    print("Press 4 for InsertionSort method of String")
    print("Press 5 for bubbleSort method of Integer")
    print("Press 6 for bubbleSort method of String")

    x =  int(input("Enter your choice"))
    if x==1:
        value = Utility.integerList()
        value.sort()
        element = int(input("Enter the element you want to search :"))
        result = Utility.binarySearch(value , element)
        if result == -1:
            print("Not found")
        else:
            print("found at index" , result)

    elif x == 2:
        value = Utility.stringList()
        value.sort()
        element = input("Enter the element for search")
        result = Utility.binarySearch(value,element)
        if result == -1:
            print("Not found")
        else:
            print("Found at index " ,result)

    elif x == 3:
        val = Utility.integerList()
        print(Utility.insertionSort1(val))

    elif x == 4:
        val = Utility.stringList()
        print(Utility.insertionSort1(val))

    elif x == 5:
        val = Utility.integerList()
        print(Utility.bubbleSort(val))

    elif x == 6:
        val = Utility.stringList()
        print(Utility.bubbleSort(val))

    else :
        print("Invalid Input")
except Exception as e:
    print("Invalid input")


