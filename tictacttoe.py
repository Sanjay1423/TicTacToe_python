board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = "X"
game_running = True
winner = None

# create a board


def createBoard(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('---------')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('---------')
    print(board[6]+' | '+board[7]+' | '+board[8])


# input


def userInput(board):
    inp = int(input('Enter a number between 0 - 9:'))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = current_player
    else:
        print('Wrong input')


# check win or tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def checkTie(board):
    if '-' not in board:
        createBoard(board)
        print('Tie!')
        game_running = False


def checkWin(board):
    global game_running
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
        createBoard(board)
        print(f'The winner is {winner}')
        game_running = False


# change the player

def changePlayer():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# again check win or tie
while game_running:
    createBoard(board)
    userInput(board)
    checkWin(board)
    checkTie(board)
    changePlayer()
