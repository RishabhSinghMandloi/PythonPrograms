# @Purpose To guess the question Number
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018




from UtitlitiesMethod import Utility

import math

try:
    noOfTimes = int(input(" How much time you want to ask the questions "))
    low = 0
    high = int(math.pow(2,noOfTimes))
    print(" Think of a Number between (" ,low,")to( " , high , ") in range ")
    result = Utility.question(low , high)
    print(result)
except Exception as e:
    print(" Enter the valid input")

