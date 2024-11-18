class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = 3

    def print_board(self, board):
        for row in board:
            print(' '.join(str(cell) for cell in row))
        print()

    def get_position(self, board, value):
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == value:
                    return i, j

    def move_blank(self, board, direction):
        x, y = self.get_position(board, 0)
        new_board = [row[:] for row in board]

        if direction == "up" and x > 0:
            new_board[x][y], new_board[x-1][y] = new_board[x-1][y], new_board[x][y]
        elif direction == "down" and x < self.n - 1:
            new_board[x][y], new_board[x+1][y] = new_board[x+1][y], new_board[x][y]
        elif direction == "left" and y > 0:
            new_board[x][y], new_board[x][y-1] = new_board[x][y-1], new_board[x][y]
        elif direction == "right" and y < self.n - 1:
            new_board[x][y], new_board[x][y+1] = new_board[x][y+1], new_board[x][y]
        else:
            return None

        return new_board

    def dfs(self, board, depth_limit=50):
        stack = [(board, [])]
        visited = set()
        directions = ["up", "down", "left", "right"]

        while stack:
            current_board, path = stack.pop()

            print("Current board:")
            self.print_board(current_board)
            print("Moves so far:", path)

            if current_board == self.goal:
                return path

            board_tuple = tuple(tuple(row) for row in current_board)
            if board_tuple in visited:
                continue
            visited.add(board_tuple)

            if len(path) >= depth_limit:
                continue

            for direction in directions:
                new_board = self.move_blank(current_board, direction)
                if new_board is not None:
                    stack.append((new_board, path + [direction]))

        return None

def get_user_input():
    print("Enter the initial configuration of the 8-puzzle (row by row, use 0 for the blank space):")
    board = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must contain 3 numbers. Try again.")
            return get_user_input()
        board.append(row)
    return board

def get_goal_input():
    print("Enter the goal configuration of the 8-puzzle (row by row, use 0 for the blank space):")
    goal = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must contain 3 numbers. Try again.")
            return get_goal_input()
        goal.append(row)
    return goal

if __name__ == "__main__":
    initial_board = get_user_input()
    goal_board = get_goal_input()

    puzzle = Puzzle(initial_board, goal_board)
    print("\nInitial board:")
    puzzle.print_board(initial_board)

    result = puzzle.dfs(initial_board, depth_limit=50)
    
    if result is None:
        print("No solution found within the depth limit.")
    else:
        print("Solution found!")
        print("Moves:", result)
