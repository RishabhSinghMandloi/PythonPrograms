try :
    number = int(input("Enter the number \n"))
    sum = 0
    for x in range (1,number):
        sum = sum + 1/x
except Exception as e :
    print("Enter the number not characters ")

print("The ", number, "th harmonic value is ", sum)





