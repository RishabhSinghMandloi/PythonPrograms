# @Purpose To find the percentage of number of  wins and loss
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility
try :
     numberOfTimes = int(input(" How many times you want to flip the coins \n"))
     if(numberOfTimes > 0) :
        Utility.flipCoins(numberOfTimes)
     else:
          print("You must atleast flip the coin once")
except Exception as e :
    print("Please enter a digit not characters")