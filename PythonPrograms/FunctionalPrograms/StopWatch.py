# @Purpose To find the elapsed time between start and stop
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018




from UtitlitiesMethod import Utility

try:
    start = int(input("press 1 to start the watch \n"))
    if start==1 :
        Utility.start()
    else:
        print("Enter 1 to start the timer \n")
        print("Wait for some time")


    stop = int(input("Press 0 to stop the watch \n"))
    if stop ==0:
        Utility.stop()
    else:
        exit(0)

    Utility.elapsedTime()

except Exception as e :
    print("Enter the valid input")
