import math

# Define the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(board, spot, player):
    board[spot] = player

def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return ' ' not in board

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_board_full(board)

def minimax(board, depth, alpha, beta, maximizing_player):
    if is_winner(board, 'O'):
        return {'score': 1 * (len(available_moves(board)) + 1)}
    elif is_winner(board, 'X'):
        return {'score': -1 * (len(available_moves(board)) + 1)}
    elif is_board_full(board):
        return {'score': 0}

    if maximizing_player:
        max_eval = {'score': -math.inf}
        for move in available_moves(board):
            board[move] = 'O'
            evaluation = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            evaluation['move'] = move
            if evaluation['score'] > max_eval['score']:
                max_eval = evaluation
            alpha = max(alpha, evaluation['score'])
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = {'score': math.inf}
        for move in available_moves(board):
            board[move] = 'X'
            evaluation = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            evaluation['move'] = move
            if evaluation['score'] < min_eval['score']:
                min_eval = evaluation
            beta = min(beta, evaluation['score'])
            if beta <= alpha:
                break
        return min_eval

def play_game():
    while True:
        print_board()
        if is_winner(board, 'O'):
            print("O wins!")
            break
        elif is_winner(board, 'X'):
            print("X wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # Player X (Human)
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        make_move(board, move, 'X')

        # Player O (AI)
        if not game_over(board):
            ai_move = minimax(board, 0, -math.inf, math.inf, True)['move']
            make_move(board, ai_move, 'O')

if __name__ == "__main__":
    play_game()
