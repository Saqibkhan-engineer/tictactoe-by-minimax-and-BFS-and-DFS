import math

PLAYER = 'X'  # Human
AI = 'O'      # Computer
EMPTY = ' '

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def is_moves_left(board):
    return any(cell == EMPTY for row in board for cell in row)

def check_winner(board):
    lines = (
        board[0], board[1], board[2],                         # rows
        [board[0][0], board[1][0], board[2][0]],              # columns
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],              # diagonals
        [board[0][2], board[1][1], board[2][0]]
    )
    for line in lines:
        if line.count(PLAYER) == 3:
            return PLAYER
        if line.count(AI) == 3:
            return AI
    return None

def is_terminal(board):
    return check_winner(board) is not None or not is_moves_left(board)

# Minimax with alpha-beta and depth-based scoring
def minimax(board, depth, alpha, beta, maximizingPlayer):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == PLAYER:
        return depth - 10
    elif not is_moves_left(board):
        return 0

    if maximizingPlayer:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def play_game():
    board = create_board()
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    break
                else:
                    print("Cell already occupied! Try again.")
            except:
                print("Invalid input! Try again.")

        print_board(board)

        if check_winner(board) == PLAYER:
            print("🎉 Player wins!")
            break
        if not is_moves_left(board):
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        print(f"AI chooses: {ai_move}")
        board[ai_move[0]][ai_move[1]] = AI
        print_board(board)

        if check_winner(board) == AI:
            print("💻 AI wins!")
            break
        if not is_moves_left(board):
            print("🤝 It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
