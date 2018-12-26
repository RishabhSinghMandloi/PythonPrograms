from UtitlitiesMethod import Utility
try :
    data = input("Enter your string \n")
    data1 = list(data)

    for p in Utility.permutation(data1) :
        print(p)

except Exception as e :
    print("Invalid input")


