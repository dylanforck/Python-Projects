#Dylan Forck
#Description: Game - Nine heads and tails



#Define the player input function
def playerInput():

    #Request player input for a number between 0 and 511
    number = int(input("Enter a number between 0 and 511: "))

    #While loop to validate that input is between 0 and 511
    while number < 0 or number > 511:

        #Request player input for a number between 0 and 511
        number = int(input("Enter a number between 0 and 511: "))

    #Return the number variable
    return number

#Define the binary conversion function
def binaryConversion(number):

    #Convert number using binary function
    binary = bin(number)

    #Remove first 2 characters to format binary number
    binary = binary.replace("0b",'')

    #While loop to add 0 to the front of binary until it is 9 characters
    while len(binary) < 9:
        binary = '0' + binary

    #Return the binary variable
    return binary

#Define the heads tails function
def headsTails(binary):

    #Replace 0 with H
    binaryString = binary.replace('0','H')

    #Replace 1 with T
    binaryString = binaryString.replace('1','T')

    #Return the binary string variable
    return binaryString

#Define the display grid
def displayGrid(binaryString):

    #Initialize index variable at 0
    index = 0

    #Loop for 3 rows
    for row in range(3):

        #Loop for 3 columns
        for column in range(3):

            #Display the indexed character
            print(binaryString[index], end = ' ')

            #Increment index variable by 1
            index += 1

        #Print a new line
        print()

#Define the nine heads and tails function
def nineHeadsAndTails():

    #Invoke the player input function 
    number = playerInput()

    #Invoke the binary conversion function
    binary = binaryConversion(number)

    #Invoke the heads tails function
    binaryString = headsTails(binary)

    #Invoke the binary string function
    displayGrid(binaryString)

#Invoke the nine heads and tails function
nineHeadsAndTails()
    
