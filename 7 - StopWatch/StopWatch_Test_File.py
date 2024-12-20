#Dylan Forck
#Description: StopWatch - Test File



#Import Stop Watch Class
from StopWatch import StopWatch

#Create the test function
def test():

    #Create the stop watch object
    stopWatch = StopWatch()

    #Start the stop watch using the dot operator
    stopWatch.start()

    #Initalize the total variable as zero
    total = 0

    #For loop to iterate 1 million times
    for value in range(1, 1000001):

        #Increment total by value in loop
        total += value

    #Stop the stop watch using the dot operator
    stopWatch.stop()

    #Display the elapsed time
    print(f"Elapsed Time: {stopWatch.getElapsedTime():.2f} Milliseconds")
    
#Invoke the test function
test()
