#Dylan Forck
#Description: The Stock Class - Test File



#Import Stock Class
from Stock_Class import Stock

#Create the test function
def test():

    #Create the stock object for Intel
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

    #Display the stock symbol using the dot operator
    print(f"Stock Symbol: {stock.getSymbol()}")

    #Display the stock name using the dot operator
    print(f"Stock Name: {stock.getName()}")

    #Display the previous closing price using the dot operator
    print(f"Previous Closing Price: ${stock.getPreviousClosingPrice():.2f}")

    #Display the current price using the dot operator
    print(f"Current Price: ${stock.getCurrentPrice():.2f}")

    #Display the price-change percentage using the dot operator
    print(f"Price-Change Percentage: {stock.getChangePercent():.2f}%")
    
#Invoke the test function
test()
