import random
import numpy as np
import math
import  time

## @Purpose: All the methods are defined in this file from here all the methods will be imported
##   @Aurthor: Rishabh Singh
##   @since  :  23-12-2018


## In this method we take the user name as input in the form of String
##  @param name


def replaceString(name):
     if len(name) > 3 :         ##ensures that length name must have atleast three characters
         print("Hello" , name , " How are you")
     else :
         print("Your name must have atleast three characters")


## In this method we get to know the occurance of number of heads and tail
## and there percentage

def flipCoins(n):
    head =0
    tail =0  #initialization

    for x in range(n):
        x = random.random()
        if(x<0.5):
            tail += 1
        else :
            head += 1

    totalnoOfHeads = head
    totalnoOfTails = tail

    print("Occurance of head " , head)
    print("Occurance of tail " , tail)

    print("HeadPercentage : ", (totalnoOfHeads/n) *100)
    print("TailPercentage : ", (totalnoOfTails/n) * 100)

## In this method we ensure weather the year is leap year or not
## @param year

def leapYear(year):

    if((year%4 == 0 and year%100 != 0 ) or (year%400 == 0)):
        print("The entered year is Leap Year")
    else :
        print("The entered is not a leap year")


## In this method we print the power of two
## @param base and x

def printTable(n):
    i=0
    while(i <= n) :
        print(i , "------" , pow(2,i))
        i +=1


def checkPrime(n):
    i=2
    while(i<=n/2):
        if(n%i==0):
            return False
        i+=1

    return True

##*****************PrimeFactor******************************##
def primeFactor(n):
    for x in range(2,n):
        if(checkPrime(x) and n%x==0):
            print(x)
##************************ Gambler ****************************##
def gambler(stack , goal , bet):
    loss = 0
    win = 0
    turns = 0

    while(stack >= 0 and stack <= goal):
        n = random.randrange(2)
        if(n==0):
            stack=stack-bet
            loss -= 1
        else:
            stack = stack+bet
            win += 1
    turns = loss + win
    calulatePercentage(win,loss,turns)
    return  win


##***********************

def calulatePercentage(win,loss,turns):
    winPercent = (win/turns)*100
    lossPercent = (loss/turns)*100

    print("WinPercentage ",winPercent)
    print("LossPercentage ",lossPercent)

##***************************** Coupans *********************************##
def coupans(list):
    count = 0
    while(len(list) > 0):
        x = random.randint(0, 9)
        count += 1
        if x in list:
            list.remove(x)
            print(list)

    print("Total random number needed to have all distinct copuans ",count)

##****************************** TwoDimensional Array *************************##
def twoDimensionalArray(x,y):
    arr= [[0 for i in range(x)]for j in range(y)]

    for i in range(x):
        for j in range(y):
            arr[i][j] = int(input("Entered elements :"))

    array=np.array(arr)
    print(array)

##*********************************Triplet*********************************************##

def findTriplet(arr):
    n = len(arr)
    count = 0
    for i in range(0,n-2,1):
        for j in range(i+1,n-1,1):
            for k in range(j+1,n,1):
                if(int(arr[i])+ int(arr[j]) + int(arr[k]) ==0):
                    print(arr[i], " ", arr[j], " ", arr[k])
                    count +=1
    print("Number of triplets " ,count)

    if(count==0):
        print("Triplet does not exist")


##********************************** StopWatch *************************************************##

def start():
    start.startTimer = time.time()
    print("Start Time : ",start.startTimer)


def stop():
    stop.stopTimer = time.time()
    print("Stop Time :",stop.stopTimer)


def elapsedTime():
    elapsed = stop.stopTimer - start.startTimer
    print()
    print("ElapsedTime :",elapsed)



##*****************************Distance*************************##

def distanceCalculation(x,y):
    distance = math.sqrt((x*x) + (y*y))
    print("Distance from origin is ",distance)

##******************************* Permutations of all Strings ***********************##

def permutation(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        l = []
        for i in range(len(list)):
            x =list[i]
            xs = list[:i] + list[i+1:]
            for p in permutation(xs):
                l.append([x] + p)
                return l

##********************************* Quadratic Equation *******************************##

def quadraticFunctions(a,b,c):

    print("Given quadratic equation is:" ,a,"x^2 +",b,"x + ",c)
    d = (b*b) - (4*a*c)
    if(d > 0):
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d))/(2*a)
        root2 = (-b-math.sqrt(d))/(2*a)
        print("First Root ",root1)
        print("Second Root " ,root2)

    elif(d==0):
        print("Roots are real and equal")
        root1 = (-b+math.sqrt(d))/(2*a)
        print("First Root ",root1)

    else:
        print("Root are imaginary")

##******************************* Windchill *******************************************************##

def windChill(temprature,windspeed):
    if(temprature < 50 and (windspeed > 3 and windspeed < 120)):
        windChill = 35.74 + 0.6215 * temprature + (0.4275*temprature - 35.75)*math.pow(windspeed,0.16)
        print()
        print("WindChill is ",windChill)
    else:
        print("Enter valid input")

##**************************************** Anagram ********************************##

def isAnagram(str1,str2):
    word1 = str1
    l1=list(word1)
    word2 = str2
    l2 = list(word2)
    if(sorted(l1)==sorted(l2)):
        print("Strings are Anagram")
    else:
        print("String are not a Anagram")

def isPalindrome(n):
    m = n
    sum = 0
    while(n!=0):
        r = n%10
        sum = sum*10 + r
        n = n/10
    if(sum == m):
        return True
    return False


def inputIntegerList():
    n= int(input("Enter no of Elements :"))
    print("Enter elements")
    listArr = [input() for i in range(n)]
    return listArr

def inputStringList():
    n=(input("Enter no of elements :"))
    print("Enter Strings :")
    listArr = [input() for i in range(n)]
    return listArr

def binarySearch(listArr,low,high,element):
    if(low>high):
        return -1
    mid = (low+high)//2
    if(listArr[mid]==element):
        return element
    if(element < mid):
        return binarySearch(listArr,low,mid-1,element)
    else:
        return binarySearch(listArr,mid+1,high,element)


def insertionSort(arr):
    n=len(arr)
    for x in range (1,n):
        key = arr[x]
        j = x - 1
        while(j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr


