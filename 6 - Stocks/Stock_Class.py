#Dylan Forck
#Description: The Stock class



#Create the Stock Class
class Stock:

    #Create the Stock Constructor
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):

        #Private data fields for symbol, name, previous closing price, and current price
        self.__symbol = symbol 
        self.__name = name 
        self.__previousClosingPrice = previousClosingPrice 
        self.__currentPrice = currentPrice 

    #Method to get the symbol
    def getSymbol(self):

        #Get symbol
        return self.__symbol

    #Method to get the name
    def getName(self):

        #Get name
        return self.__name

    #Method to get the previous closing price
    def getPreviousClosingPrice(self):

        #Get previous closing price
        return self.__previousClosingPrice

    #Method to get the current price
    def getCurrentPrice(self):

        #Get current price
        return self.__currentPrice

    #Method to set the previous closing price
    def setPreviousClosingPrice(self, previousClosingPrice):

        #Set previous closing price
        self.__previousClosingPrice = previousClosingPrice

    #Method to set the current price
    def setCurrentPrice(self, currentPrice):
        
        #Set current price
        self.__currentPrice = currentPrice

    #Method to get the percentage changed from previous closing price to current price
    def getChangePercent(self):
        
        #Calculate change amount equal to current price minus previous closing price
        changeAmount = self.__currentPrice - self.__previousClosingPrice
        
        #Calculate change percent equal to change amount divided by previous closing price
        changePercent = (changeAmount / self.__previousClosingPrice)

        #Convert change percent to percentage by multiplying by 100
        changePercent = changePercent * 100

        #Get change percent
        return changePercent   
