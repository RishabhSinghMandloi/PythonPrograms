from UtitlitiesMethod import Utility

try:
    temp = int(input("Enter temprature \n"))
    windSpeed = int(input("Enter the windSpeed \n"))
    Utility.windChill(temp,windSpeed)
except:
    print("Enter the valid input")
