import random
import numpy as np
import math
import time


## @Purpose: All the methods are defined in this file from here all the methods will be imported
##   @Aurthor: Rishabh Singh
##   @since  :  23-12-2018


# In this method we take the user name as input in the form of String
# @param name


def replaceString(name):
    if len(name) > 3:  ##ensures that length name must have atleast three characters
        print("Hello", name, " How are you")
    else:
        print("Your name must have atleast three characters")


## In this method we get to know the occurance of number of heads and tail
## and there percentage

def flipCoins(n):
    head = 0
    tail = 0  # initialization

    for x in range(n):
        x = random.random()  # predifined method present in random package

        if (x < 0.5):
            tail += 1
        else:
            head += 1

    totalnoOfHeads = head
    totalnoOfTails = tail

    print("Occurance of head ", head)
    print("Occurance of tail ", tail)

    print("HeadPercentage : ", (totalnoOfHeads / n) * 100)
    print("TailPercentage : ", (totalnoOfTails / n) * 100)


## In this method we ensure weather the year is leap year or not
## @param year

def leapYear(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("The entered year is Leap Year")
    else:
        print("The entered is not a leap year")


## In this method we print the power of two
## @param base and x

def printTable(n):
    i = 0
    while (i <= n):
        print(i, "------", pow(2, i))
        i += 1


## In this method we check weather the number is prime or not
## and it returns the corresponding boolean value


def checkPrime(n):
    i = 2
    while (i <= n / 2):
        if (n % i == 0):
            return False
        i += 1

    return True


## this method is used to find the prime factors of the number


def primeFactor(n):
    for x in range(2, n):
        if (checkPrime(x) and n % x == 0):  ##checkPrime method checks weather the number is prime or not
            print(x)


##this method is we find the percentage of wins and loss
## @param stack
## @param goal
## @param bet


def gambler(stack, goal, bet):
    loss = 0
    win = 0
    turns = 0

    while (stack >= 0 and stack <= goal):
        n = random.randrange(2)
        if (n == 0):
            stack = stack - bet
            loss -= 1
        else:
            stack = stack + bet
            win += 1
    turns = loss + win
    calulatePercentage(win, loss, turns)
    return win


# In this method we calucate the percentage
## @param win
## @param loss
## @param turns


def calulatePercentage(win, loss, turns):
    winPercent = (win / turns) * 100
    lossPercent = (loss / turns) * 100

    print("WinPercentage ", winPercent)
    print("LossPercentage ", lossPercent)


## In this method we find the Number of times the random number is genrated to
## find the distnict number of coupans


def coupans(list):
    count = 0
    while (len(list) > 0):
        x = random.randint(0, 9)
        count += 1
        if x in list:
            list.remove(x)
            print(list)

    print("Total random number needed to have all distinct copuans ", count)


## In this method we read the matrix from the user
##  @param x
## @param  y


def twoDimensionalArray(x, y):
    arr = [[0 for i in range(x)] for j in range(y)]

    for i in range(x):
        for j in range(y):
            arr[i][j] = int(input("Entered elements :"))

    array = np.array(arr)
    print(array)


##*********************************Triplet*********************************************##
## In this method we find the triplet which gives us the sum of zero
## and also we count how many triplets are present


def findTriplet(arr):
    n = len(arr)
    count = 0
    for i in range(0, n - 2, 1):
        for j in range(i + 1, n - 1, 1):
            for k in range(j + 1, n, 1):
                if (int(arr[i]) + int(arr[j]) + int(arr[k]) == 0):
                    print(arr[i], " ", arr[j], " ", arr[k])
                    count += 1
    print("Number of triplets ", count)

    if (count == 0):
        print("Triplet does not exist")


## this method evaluates the start time


def start():
    start.startTimer = time.time()  ## this is a predefined method present in time package
    print("Start Time : ", start.startTimer)


## this method evaluates the stop time

def stop():
    stop.stopTimer = time.time()  ## this is a predifined method present in time package
    print("Stop Time :", stop.stopTimer)


## this method calculate the  elapsed time between start time and stop time
def elapsedTime():
    elapsed = stop.stopTimer - start.startTimer
    print()
    print("ElapsedTime :", elapsed)


## this method evaluates the distance of a coordinates from the origin
##  and calculate its value
## @param x
## @param y


def distanceCalculation(x, y):
    distance = math.sqrt((x * x) + (y * y))
    print("Distance from origin is ", distance)


## To find all the permutation of the string
## @param list


def permutation(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        l = []
        for i in range(len(list)):
            x = list[i]
            xs = list[:i] + list[i + 1:]
            for p in permutation(xs):
                l.append([x] + p)
            return l


# To find the roots of the quadratic equation weather they are real, unequal or imagianry
# @param a
# @param b
# @param c


def quadraticFunctions(a, b, c):
    print("Given quadratic equation is:", a, "x^2 +", b, "x + ", c)
    d = (b * b) - (4 * a * c)
    if (d > 0):
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("First Root ", root1)
        print("Second Root ", root2)

    elif (d == 0):
        print("Roots are real and equal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("First Root ", root1)

    else:
        print("Root are imaginary")


# To evaluate the temprature with the help of natioanl weather service windchill formula


def windChill(temprature, windspeed):
    if (temprature < 50 and (windspeed > 3 and windspeed < 120)):
        windChill = 35.74 + 0.6215 * temprature + (0.4275 * temprature - 35.75) * math.pow(windspeed, 0.16)
        print()
        print("WindChill is ", windChill)
    else:
        print("Enter valid input")


# To find weather the two strings are anagram or not
# Strings are anagram if simply the  same type of characters are present in both Strings


def isAnagram(str1, str2):
    word1 = str1
    l1 = list(word1)
    word2 = str2
    l2 = list(word2)
    if (sorted(l1) == sorted(l2)):
        print("Strings are Anagram")
    else:
        print("String are not a Anagram")


#  this method finds out weather the number is paliortome or not
# palindrome means if the number is reversed it same as pervious


def Palindrome(n):
    m = n
    sum = 0
    while (n != 0):
        r = n % 10
        sum = sum * 10 + r
        n = n / 10
    if (sum == m):
        return True
    return False


# this method is used to take the integer type input in list


def inputIntegerList():
    n = int(input("Enter no of Elements :"))
    print("Enter elements")
    listArr = [input() for i in range(n)]
    return listArr


# this methos is used to take the String type input in the list


def inputStringList():
    n = (input("Enter no of elements :"))
    print("Enter Strings :")
    listArr = [input() for i in range(n)]
    return listArr


# this method is used for sorted array in binary search we  search for an element inside the array
# with the help of recursion


def binarySearch1(listArr, low, high, element):
    if (low > high):
        return -1
    mid = (low + high) // 2
    if (listArr[mid] == element):
        return element
    if (element < mid):
        return binarySearch1(listArr, low, mid - 1, element)  ##using recursioin
    else:
        return binarySearch1(listArr, mid + 1, high, element)  ## using  recursion


# this method is used for sorted array in binary search we  search for an element inside the array


def binarySearch(arr, x):
    start = 0
    end = len(arr) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (x == arr[mid]):
            return mid

        if (x < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return -1


# In insertion sort method we sort the element by comparing its next elemnt
# if the next element is smaller simply we swap it with the previous element


def insertionSort1(arr):
    n = len(arr)
    for x in range(1, n):
        key = arr[x]
        j = x - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]  # swaping of elements
            j = j - 1
        arr[j + 1] = key
    return arr


# In insertion sort method we sort the element by comparing its next elemnt
# if the next element is smaller simply we swap it with the previous element


def insertionSort(arr):
    for i in arr:
        j = arr.index(i)

        while (j > 0):
            # not in order
            if arr[j - 1] > arr[j]:
                # swap
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
            j = j - 1
    print(arr)


# this method is used to read the elements inside the array


def readArray():
    a = int(input("Enter total number of elements "))
    li = []
    for i in range(0, a):
        x = input("enter element")
        li.append(x)
    print(li)


# to evaluate weather the number is prime or not

def isPrime(start, end):
    for value in range(start, end + 1):
        #if value > 1:
            for n in range(2, value):
                if (value % n) == 0:
                    break
            else:
                isPalindrome(value)
                print(value)


#  this method finds out weather the number is paliortome or not
# palindrome means if the number is reversed it same as pervious


def isPalindrome(value):
    temp = value
    sum = 0
    while (value > 0):
        rem = value % 10
        sum = sum * 10 + rem
        value = value // 10
        if (temp == sum):
            print(temp)


# In bubble sort method we simply comapre one element to the next element
# In this method we swap one element with next element


def bubbleSort(listArr):
    temp = 0
    for i in range(0, len(listArr) - 1, 1):
        for j in range(1, len(listArr), 1):
            if (listArr[j - 1]) > listArr[j]:
                temp = listArr[j - 1]
                listArr[j - 1] = listArr[j]  ## swapping of elements
                listArr[j] = temp
    return listArr


# this method is used take the integer type input in the list


def integerList():
    n = int(input("Enter no of Elements you want"))
    listArr = []
    for i in range(n):
        x = int(input("Enter values"))
        listArr.append(x)
    return listArr


## this method is used to take the String type input in  the list
def stringList():
    n = int(input("Enter the number of words you want"))
    listArr = []
    for i in range(n):
        x = input("Enter words")
        listArr.append(x)
    return listArr


## method to return the day which is present on the current date
## by using the below formula
def dayOfWeek(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    day = (d + x + 31 * m0 // 12) % 7

    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursady")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    else:
        print("Invalid input")


## to calculate the monthly payment which we have to give on the principal amount
## on the given rate of intrest and within the given time peroid


def monthlyPayment(p, y, r):
    n = 12 * y
    r0 = r / (12 * 100)
    pay = (p * r0) / (1 - math.pow(1 + r0 - n))
    print("Mothly payment is ", pay)


## to determine the temprature in farahnite as well as in celsius

def tempratureConversion(celsius, farhanite):
    celsiusTemp = (farhanite - 32) * 5 // 9
    print("Teamprature in celsius :", celsiusTemp)
    farhaniteTemp = (celsius * 9 // 5) + 32
    print("Temprature in faheranite :", farhaniteTemp)
