import math

# Define the board
board = [' ' for _ in range(9)]  # A single list to represent a 3x3 board

def print_board():
    print('---------')
    for i in range(3):
        print('|', board[3*i], '|', board[3*i+1], '|', board[3*i+2], '|')
    print('---------')

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            board[int(move) - 1] = 'X'
            break
        else:
            print("Invalid move. Please try again.")

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()

        if check_winner('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner('O'):
            print("Sorry, you lose!")
            break
        if check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
