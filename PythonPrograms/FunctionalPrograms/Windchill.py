# @Purpose To evaluate the tempratue with the help of windchill formula
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility

try:
    temp = int(input("Enter temprature \n"))
    windSpeed = int(input("Enter the windSpeed \n"))
    Utility.windChill(temp,windSpeed)
except:
    print("Enter the valid input")
