#Dylan Forck
#Description: The Account class



#Create the Account Class
class Account:

    #Create the Account Constuctor
    def __init__(self, id = int(0), balance = float(100), annualInterestRate = float(0)):

        #Private data fields for id, balance, and annual interest rate
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    #Method to get the id
    def getId(self):

        #Get id
        return self.__id

    #Method to get the balance
    def getBalance(self):

        #Get Balance
        return self.__balance

    #Method to get the annual interest rate
    def getAnnualInterestRate(self):

        #Get annual interest rate
        return self.__annualInterestRate

    #Method to set the id
    def setId(self, id):

        #Set id
        self.__id = id

    #Method to set the balance
    def setBalance(self, balance):

        #Set balance
        self.__balance = balance

    #Method to set the annual interest rate
    def setAnnualInterestRate(self, annualInterestRate):

        #Set annual interest rate
        self.__annualInterestRate = annualInterestRate

    #Method to get the monthly interest rate
    def getMonthlyInterestRate(self):

        #Get the annual interest rate
        annualInterestRate = self.__annualInterestRate

        #Divide annual interest rate by 12 to convert it from yearly to monthly
        monthlyInterestRate = annualInterestRate / 12
    
        #Get monthly interest rate
        return monthlyInterestRate

    #Method to get the monthly interest amount
    def getMonthlyInterest(self):

        #Create monthly interest rate by invoking get monthly interest rate method
        monthlyInterestRate = self.getMonthlyInterestRate()

        #Divide monthly interest rate by 100 to convert it from percentage to decimal
        monthlyInterestRate = monthlyInterestRate / 100

        #Create monthly interest amount by multiplying monthly interest rate by balance
        monthlyInterest = self.__balance * monthlyInterestRate

        #Get monthly interest amount
        return monthlyInterest

    #Method to withdraw from balance based on amount
    def withdraw(self, amount):

        #Set balance by decrementing for the amount of withdrawal
        self.__balance -= amount

    #Method to deposit to balance based on amount
    def deposit(self, amount):

        #Set balance by incrementing for the amount of deposit
        self.__balance += amount 

