def solveNQueens(N):
    solutions = []
    board = [['.'] * N for _ in range(N)]
    col = set()
    posDiag = set()
    negDiag = set()

    def bt(r):
        if r == N:
            solutions.append(["".join(row) for row in board])
            return
        
        for c in range(N):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            
            board[r][c] = 'Q'
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            
            bt(r + 1)
            
            board[r][c] = '.'
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)

    bt(0)
    return solutions

def printSolutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(' | '.join(row))
        print("-" * (4 * len(solution) - 1))
        print()

N = int(input("Enter the size of the board (N): "))
solutions = solveNQueens(N)

if solutions:
    print(f"Found {len(solutions)} solutions for {N}-Queens Problem.")
    printSolutions(solutions)
else:
    print("No solutions found.")
