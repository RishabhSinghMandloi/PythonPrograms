import sys

num = int(sys.argv[1])

if num >=0 :
    if num < 31:
        for i in range(0, num+1):
            print(i, " ----> ", 2**i)
    else:
        print("Value should less than 31")
else:
    print("Value should greater than or equals to 0")
