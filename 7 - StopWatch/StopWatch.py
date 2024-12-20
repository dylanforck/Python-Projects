#Dylan Forck
#Description: Stopwatch




#Import the time module
import time

#Create the StopWatch Class
class StopWatch:

    #Create the StopWatch Constructor
    def __init__(self):

        #Private data field for start time initialized to current time
        self.__startTime = time.time()

        #Private data field for end initalized to zero as a float value
        self.__endTime = float(0)

    #Method to get the start time
    def getStartTime(self):

        #Get start time
        return self.__startTime

    #Method to get the end time
    def getEndTime(self):

        #Get end time
        return self.__endTime

    #Method to set the start time
    def start(self):

        #Set start time to current time
        self.__startTime = time.time()

    #Method to set the end time
    def stop(self):

        #Set end time to current time
        self.__endTime = time.time()  

    #Method to get the elapsed time for the stop watch
    def getElapsedTime(self):
        
        #Calculate elapsed time from end time minus start time
        elapsedTime = self.__endTime - self.__startTime

        #Convert elapsed time from seconds to milliseconds
        elapsedTime = elapsedTime * 1000

        #Get elapsed time 
        return elapsedTime   
