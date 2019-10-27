# Two person tic-tac-toe game written by yours truly
import array

gameState = True

Board = [[2,2,2], [2,2,2], [2,2,2,]]

def printBoard():
    for i in Board:
        for c in i:
            print(c,end = " ")
        print()

#while gameState:

printBoard()


