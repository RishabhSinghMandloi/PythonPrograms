# @Purpose To find the current day present on given date
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility

try:
    day = int(input("Enter day [1 - 31]: "))
    if(day < 1 and day > 32):
        print("Enter valid input in given range")

    month = int(input("Enter month[1-12]:"))
    if(day < 1 and day > 12):
        print("Enter the valid input in the given range")

    year = int(input("Enter year[1000 - 9999]:"))
    if(day<1000 and day > 9999):
        print("Enter the valid input in given range")

    Utility.dayOfWeek(day,month,year)

except Exception as e:
    print("Plese enter the valid data")
