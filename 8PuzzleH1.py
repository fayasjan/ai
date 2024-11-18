import heapq

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

    def manhattan_distance(self, board):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                value = board[i][j]
                if value != 0:
                    goal_x, goal_y = self.get_position(self.goal, value)
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def a_star(self, board):
        open_list = []
        heapq.heappush(open_list, (0 + self.manhattan_distance(board), 0, board, []))
        closed_list = set()
        visited = set()
        directions = ["up", "down", "left", "right"]

        while open_list:
            f, g, current_board, path = heapq.heappop(open_list)

            if current_board == self.goal:
                return path

            board_tuple = tuple(tuple(row) for row in current_board)
            if board_tuple in visited:
                continue
            visited.add(board_tuple)

            for direction in directions:
                new_board = self.move_blank(current_board, direction)
                if new_board is not None:
                    new_g = g + 1
                    new_f = new_g + self.manhattan_distance(new_board)
                    heapq.heappush(open_list, (new_f, new_g, new_board, path + [direction]))

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

    result = puzzle.a_star(initial_board)
    
    if result is None:
        print("No solution found.")
    else:
        print("Solution found!")
        print("Moves:", result)
