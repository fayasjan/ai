def print_board(board):
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i != 2:
            print("-" * 5)

def check_winner(board, player):
    for row in range(3):
        if all([board[row*3 + col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row*3 + col] == player for row in range(3)]):
            return True
    if all([board[i*3 + i] == player for i in range(3)]) or all([board[i*3 + (2-i)] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for cell in board])

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        if current_player == "X":
            try:
                move = int(input(f"Player {current_player}, enter the index (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid index, must be between 0 and 8. Try again.")
                    continue
                if board[move] != " ":
                    print("Cell is already taken, try again.")
                    continue
                board[move] = current_player
            except ValueError:
                print("Invalid input, please enter a number between 0 and 8.")
                continue
        else:
            print(f"AI (Player {current_player}) is making a move...")
            move = ai_move(board)
            board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
