#Dylan Forck
#Description: The Account Class - Test File



#Import Account Class
from Account_Class import Account

#Create the test function
def test():

    #Create the account object
    account = Account(1122, 20000, 4.5)

    #Withdraw method using the dot operator
    account.withdraw(2500)

    #Deposit method using the dot operator
    account.deposit(3000)

    #Display the account id using the dot operator
    print(f"Account ID: {account.getId()}")

    #Display the balance using the dot operator
    print(f"Balance: ${account.getBalance():.2f}")

    #Display the monthly interest rate using the dot operator
    print(f"Monthly Interest Rate: {account.getMonthlyInterestRate():.2f}%")

    #Display the monthly interest amount using the dot operator
    print(f"Monthly Interest: ${account.getMonthlyInterest():.2f}")
    
#Invoke the test function
test()








