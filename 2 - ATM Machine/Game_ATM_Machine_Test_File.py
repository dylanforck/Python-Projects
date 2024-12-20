#Dylan Forck
#Description: Game - ATM machine (The Account class) - Test File



#Import Account Class
from Game_ATM_Machine import Account

#Create the accounts function
def accountsList():

    #Create empty list for accounts
    accounts = []

    #For loop to assign 10 accounts from 0-9 to the list
    for a in range(10):

        #Create account id
        accountId = int(a)

        #Create the initial balance variable
        initialBalance = float(100)

        #Create the account object
        account = Account(accountId, initialBalance)

        #Append the account to the accounts list
        accounts.append(account)

    #Return accounts list
    return accounts

#Create the atm display function
def atmDisplay():

    #Print atm display lines
    print("\nMain menu")
    print("1: check balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")

    #Prompt user to input a choice
    choice = int(input("Enter a choice: "))

    #Return choice
    return choice

#Create the atm function
def atm():

    #Create the accounts list by invoking the accounts function
    accounts = accountsList()

    #While loop to keep running the system
    while True:

        #Prompt the user to input their id
        userId = int(input("Enter an account id: "))

        #Validate user input is between 0 and 9
        if 0 <= userId <= 9:

            #Access user account from accounts list
            userAccount = accounts[userId]

            #While loop for account choices
            while True:

                #Invoke the atm display and get the user's choice
                choice = atmDisplay()

                #Choice equal to 1
                if choice == 1:

                    #Display user account balance using the dot operator
                    print(f"The balance is {userAccount.getBalance():.2f}")

                #Choice equal to 2
                elif choice == 2:

                    #Prompt the user to input amount for withdrawal
                    amount = float(input("Enter an amount to withdraw: "))

                    #Withdraw method using the dot operator
                    userAccount.withdraw(amount)

                #Choice equal to 3
                elif choice == 3:

                    #Prompt the user to input amount for deposit
                    amount = float(input("Enter an amount to deposit: "))

                    #Deposit method using the dot operator
                    userAccount.deposit(amount)

                #Choice equal to 4
                elif choice == 4:

                    #Exit out of inner loop for user account
                    break

                #Choice not equal to 1 through 4
                else:

                    #Display error message
                    print("Invalid choice. Please enter a valid choice (1-4).")

        #Account not equal to 0 through 9
        else:

            #Display error message
            print("Invalid ID. Please enter a valid ID (0-9).")
    
#Invoke the atm function
atm()
