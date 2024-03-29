#Tic Tac Toe AI with help from the internet not capping
#Authored by Gavin O'Leary. Please distribute as free and open source software. See LICENSE.md

import random

def drawBoard(board):
     # This function prints out the board that it was passed.

     # "board" is a list of 10 strings representing the board (ignore index 0)
     # We ignore index 0 to be consistent thru out program and help users
     print('   |   |')
     print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
     print('   |   |')

def playPLetter():
    #Lets player choose letter they want
    #returns a list with the human letter as first item, AI letter as second
    
    letter = ""
    while not(letter == 'X' or letter =='O'):
        print("Do you want to be X or O?: ")
        letter = input().upper()
        
    # setting list elements
    
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
def FirstChoice():
    #Randomly chooses who goes first cause my programs are fair like that
    
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #Returns true if player(s) wanna keep playing
    uinput = input("Do you want to play again? (yes or no): ")
    if uinput == "yes":
        return True
    return False
def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    #Only thing I copy pasted cause this is straight dumb and time consuming and otherwise uninteresting it's really obv to us who wins just need to hard program it
    #Takes in a board and letter and allows us to check wins easily
    #Returns True for a win condition False else
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
    
def getBoardCopy(board):
    anothaOne = []
    for i in board:
        anothaOne.append(i)
    return anothaOne

def isSpaceFree(board, move):
    #Returns true if the move is free on the board
    return board[move]==""

def getPlayerMove(board):
    #Lets the human try and beat my AI
    move = ""
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the valid list on the passed board
    #Returns none if there is no valid move available
    
    #Creates a list with moves that are legal
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0: #check if the game is tied or not
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #Takes the board and the computer Letter and chooses where to return the move
    
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    
    #The meat and bones of the AI that I def didn't need a lot of help writing cause i suck
    
    #Check if we can win in one move
    for i in range(1, 10): #loops through whole board
        copy = getBoardCopy(board) #create copy board to test moves
        if isSpaceFree(copy, i): #check if the move we're testing is possible
            makeMove(copy, computerLetter, i) #test move on copy board
            if isWinner(copy, computerLetter): #if the move is a winner, we return it!
                return i
                
    #Check if the player could win in one move, and stop them
    #Same idea as above but use playerLetter instead of computerLetter to check human moves
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i) 
            if isWinner(copy, playerLetter): #if player has a winning move, play it to stop them
                return i
    
    #Try to take a corner
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move!= None:
        return move
    
    #Try to take the center
    if isSpaceFree(board, 5):
        return 5
    
    #Move on one side
    return chooseRandomMoveFromList(board, [2,4,6,8])
    
def isBoardFull(board):
    #Returns true if the game is over via full board
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
        
print("Welcome to TicTacToe!")

while True:
    #Reset Board
    
    theBoard = [''] * 10
    playerLetter, computerLetter = playPLetter()
    turn = FirstChoice()
    print("The " + turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            #players turn
            
            #Draw new board
            drawBoard(theBoard)
            #retrieve and make human move
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            #player wins lol this has yet to happen
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameisPlaying = False
            #i.e what is displayedn 99.99% of the time
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                #hand off control to the AI for its move
                else:
                    turn = 'computer'
        else:
            #Computer turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            #Check if computer move wins and leaves game if true
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Computer wins! You lose!")
                gameIsPlaying = False
            #otherwise check if the game is tied
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("This game is tied")
                    break
                #then hand off control back to human
                else:
                    turn = 'player'
    #Do we want to play again?                
    if not playAgain():
        break
