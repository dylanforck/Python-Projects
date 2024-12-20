#Dylan Forck
#Description: Game - Play a tic-tac-toe



#Define the display board function
def displayBoard(board):

    #Print the first row seperator
    print("\n-------------")

    #For loop to iterate through the rows 
    for row in board:

        #Print the first seperator
        print('|', end = ' ')

        #For loop to iterate through each column of specified row
        for column in row:

            #Print the specific value for row column index
            print(column, end = ' | ')
            
        #Print remaining row seperators
        print("\n-------------")

#Define the player input function
def playerInput(board, player):

    #Player input for row and column of their move
    row = int(input(f"Enter a row for player {player}: "))
    column = int(input(f"Enter a column for player {player}: "))

    #While loop to validate the selected cell was originally empty
    while board[row][column] != ' ':

        #Display invalid input
        print("This cell is already occupied. Try a different cell")

        #Redo player input until valid
        row = int(input(f"Enter a row for player {player}: "))
        column = int(input(f"Enter a column for player {player}: "))
        
    #Update specific matrix index with player value
    board[row][column] = player

#Define the swap player function
def swapPlayer(player):

    #Swap the player value between X and O
    if player == 'X':
        return 'O'
    else:
        return 'X'
        
#Define the check for a win Function
def checkWin(board):

    #Check for matching rows
    for row in board:

        #Check match for all three column values in specified row
        if row[0] == row[1] == row[2]:

            #Check that matching values are not blank
            if row[0] != ' ' and row[1] != ' ' and row[2] != ' ':

                #Return True if win found
                return True

    #Check for matching columns
    for column in range(3):

        #Check match for all three values in specified column
        if board[0][column] == board[1][column] == board[2][column]:

            #Check that matching values are not blank
            if board[0][column] != ' ' and board[1][column] != ' ' \
               and board[2][column] != ' ':

                #Return True if win found
                return True

    #Check for matching diagonal
    if board[0][0] == board[1][1] == board[2][2]:

        #Check that matching values are not blank
        if board[0][0] != ' ' and board[1][1] != ' ' \
               and board[2][2] != ' ':

            #Return True if win found
            return True
        
    #Check for matching diagonal
    if board[0][2] == board[1][1] == board[2][0]:

        #Check that matching values are not blank
        if board[0][2] != ' ' and board[1][1] != ' ' \
               and board[2][0] != ' ':

            #Return True if win found
            return True

    #Return False if win not found
    return False

#Define the tic tac toe function
def ticTacToe():

    #Initialize 3x3 board list as blank strings
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

    #Initialize player variable as X for starting player
    player = 'X'

    #For loop of 9 possible total moves
    for move in range(9):

        #Invoke the display board function
        displayBoard(board)

        #Invoke player input function
        playerInput(board, player)

        #Invoke check win function, if true end the game
        if checkWin(board) == True:

            #Invoke the display board function
            displayBoard(board)

            #Display the winner
            print(f"{player} player won")

            #Exit function to end game
            return

        #Swap the player after each move
        player = swapPlayer(player)

    #Invoke the display board function
    displayBoard(board)

    #Show draw once loop is done
    print("No Winner")

#Invoke the tic tac toe function
ticTacToe()

