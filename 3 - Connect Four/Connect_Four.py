#Dylan Forck
#Description: Game - Connect Four



#Define the display board function
def displayBoard(board):

    #For loop to iterate through the rows 
    for row in board:

        #Print the first seperator
        print('|', end = '')

        #For loop to iterate through each column of specified row
        for column in row:

            #Print the specific value for row column index
            print(column, end = '|')

        #Print new line for each row
        print()
            
    #Print bottom row seperator
    print("----------------------")

#Define the player input function
def playerInput(board, player, disk):

    #While loop for if column is full, ask for new input
    while True:
    
        #Player input for column of their move
        column = int(input(f"Drop a {disk} disk at column (0-6): "))

        #Initialize row variable as bottom row
        row = 5

        #While loop to iterate through rows from bottom to top
        while row >= 0:

            #Validate the selected cell was originally empty
            if board[row][column] == ' ':

                #Update specific matrix index with player value
                board[row][column] = player

                #Return to exit function
                return

            #Decrement row by 1
            row -= 1

        #Display invalid input
        print("This column is full. Try a different column")

#Define the swap player function
def swapPlayer(player):

    #Swap the player value between R and Y
    if player == 'R':
        return 'Y'
    else:
        return 'R'   

#Define the swap disk function
def swapDisk(disk):

    #Swap the disk value between red and yellow
    if disk == 'red':
        return 'yellow'
    else:
        return 'red'
       
#Define the check win function
def checkWin(board):

    #Check for matching row
    #Loop through all 6 rows
    for row in range(6):

        #Loop through first 4 columns
        for column in range(4):

            #Check match between 4 consecutive columns
            #Increment column index by 1, 2, and 3
            if board[row][column] == board[row][column + 1] == \
               board[row][column + 2] == board[row][column + 3]:

                #Check that matching values are not blank
                if board[row][column] != ' ' and board[row][column + 1] != ' ' \
                   and board[row][column + 2] != ' ' and board[row][column + 3] != ' ':

                    #Return True if win found
                    return True
    
    #Check for matching column
    #Loop through all 7 columns
    for column in range(7):

        #Loop through first 3 rows
        for row in range(3):

            #Check match between 4 consecutive rows
            #Increment row index by 1, 2, and 3
            if board[row][column] == board[row + 1][column] == \
               board[row + 2][column] == board[row + 3][column]:

                #Check that matching values are not blank
                if board[row][column] != ' ' and board[row + 1][column] != ' ' \
                   and board[row + 2][column] != ' ' and board[row + 3][column] != ' ':

                    #Return True if win found
                    return True

    #Check for matching diagonal
    #Loop through first 3 rows
    for row in range(3):

        #Loop through first 4 columns
        for column in range(4):

            #Check match between 4 consecutive diagonals
            #Increment row nand column index by 1, 2, and 3
            if board[row][column] == board[row + 1][column + 1] == \
               board[row + 2][column + 2] == board[row + 3][column + 3]:

                #Check that matching values are not blank
                if board[row][column] != ' ' and board[row + 1][column + 1] != ' ' \
                   and board[row + 2][column + 2] != ' ' and board[row + 3][column + 3] != ' ':

                    #Return True if win found
                    return True

    #Check for matching diagonal
    #Loop through last 3 rows
    for row in range(3,6):

        #Loop through first 4 columns
        for column in range(4):

            #Check match between 4 consecutive diagonals
            #Increment column index by 1, 2, and 3
            #Decrement row index by 1, 2, and 3
            if board[row][column] == board[row - 1][column + 1] == \
               board[row - 2][column + 2] == board[row - 3][column - 3]:

                #Check that matching values are not blank
                if board[row][column] != ' ' and board[row - 1][column + 1] != ' ' \
                   and board[row - 2][column + 2] != ' ' and board[row - 3][column + 3] != ' ':

                    #Return True if win found
                    return True

    #Return False if win not found
    return False

#Define the connect four function
def connectFour():

    #Initialize board list 
    board = []

    #For loop to append board with 6 rows
    for row in range(6):

        #Add an empty new row with 7 blank strings
        board.append([' '] * 7)

    #Initialize player variable as R for starting player
    player = 'R'

    #Initialize disk variable as red for starting player
    disk = 'red'

    #For loop of 42 possible total moves
    for move in range(42):

        #Invoke the display board function
        displayBoard(board)

        #Invoke player input function
        playerInput(board, player, disk)

        #Invoke check win function, if true end the game
        if checkWin(board) == True:

            #Invoke the display board function
            displayBoard(board)

            #Display the winner
            print(f"The {disk} player won")

            #Exit function to end game
            return

        #Swap the player after each move
        player = swapPlayer(player)

        #Swap the disk after each move
        disk = swapDisk(disk)

    #Invoke the display board function
    displayBoard(board)

    #Show draw once loop is done
    print("No Winner")

#Invoke the connect four function
connectFour()

   
