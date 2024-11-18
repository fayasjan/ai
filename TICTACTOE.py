import random

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

def ai_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells)

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
