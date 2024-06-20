
def print_key():
    print('Key:')
    print('_______')
    print(f'|0|1|2|')
    print('_______')
    print(f'|3|4|5|')
    print('_______')
    print(f'|6|7|8|')
    print(f'-------\n')

def print_board(board):
    print('Current Board:')
    print('_______')
    print(f'|{board[0]}|{board[1]}|{board[2]}|')
    print('_______')
    print(f'|{board[3]}|{board[4]}|{board[5]}|')
    print('_______')
    print(f'|{board[6]}|{board[7]}|{board[8]}|')
    print(f'-------')

def game_is_won(board):
    if (board[0] == board[1] == board[2] != ' ') or \
       (board[3] == board[4] == board[5] != ' ') or \
       (board[6] == board[7] == board[8] != ' ') or \
       (board[0] == board[3] == board[6] != ' ') or \
       (board[1] == board[4] == board[7] != ' ') or \
       (board[2] == board[5] == board[8] != ' ') or \
       (board[0] == board[4] == board[8] != ' ') or \
       (board[6] == board[4] == board[2] != ' '):
        return True
    else:
        return False

def get_move(board, move):
    try:
        move = int(input("Enter your move (0-8):"))
        if move not in range(9):
            print("Your move must be an integer 0-8, please refer to key.")
            return ''
        elif board[move] != ' ':
            print("Your move has already been played! Select another.")
            return ''
        else:
            return move
    except ValueError:
        print("Your move must be an integer.")
        return ''

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
player = 'X'
ongoing = True

while(ongoing):
    print_key()
    print(f"It is {player}'s turn.")
    print_board(board)
    move  = ''
    while(move == ''):
        move = get_move(board, move)
    board[move] = player
    print(f"Updated board!")
    print_board(board)
    print('\n\n')


    if game_is_won(board):
        print(f'Game won by {player}!')
        ongoing = False
    elif ' ' not in board:
        print(f'Game is a tie!')
        ongoing = False
    else:
        player = 'X' if player == 'O' else 'O'


