

print(" *** Tic Tac Game v.1.0 ***")


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',
             }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print("\n")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    
    turn = 'X'
    count = 0

    for i in range (10):
        printBoard(theBoard)
        print("\nIt's your turn," + turn + ". What's your next move?")
        
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count = count + 1
        else:
            print("That place is already filled. What's your next move?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #across the top
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #across the middle
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #across the bottom
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ': #down the left side
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ': #down the middle side
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ': #down the right side
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #diagonal 1
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break
            if theBoard['9'] == theBoard['5'] == theBoard['3'] != ' ': #diagonal 2
                printBoard(theBoard)
                print("Game Over")
                print("***" + turn + " won. ***")
                break

        if count == 9:
            print("Game Over !!")
            print("Unfortunately, It's a Tie !!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play again (Y/N)??")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = " "

game()
