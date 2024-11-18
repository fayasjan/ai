def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    indent = "    " * depth
    node_type = "Maximizing" if maximizing_player else "Minimizing"
    
    if depth == 3:
        print(f"{indent}Depth {depth} | Leaf Node {node_index} | Value: {values[node_index]}")
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        print(f"{indent}Depth {depth} | {node_type} Node {node_index} | Alpha: {alpha}, Beta: {beta}")
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            if alpha != max(alpha, eval):
                alpha = max(alpha, eval)
                print(f"{indent}Depth {depth} | Updated Alpha at Node {node_index}: {alpha}")
            if beta <= alpha:
                print(f"{indent}Depth {depth} | Pruning at Node {node_index} | Alpha: {alpha} >= Beta: {beta}")
                break
        return max_eval
    else:
        min_eval = float('inf')
        print(f"{indent}Depth {depth} | {node_type} Node {node_index} | Alpha: {alpha}, Beta: {beta}")
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            if beta != min(beta, eval):
                beta = min(beta, eval)
                print(f"{indent}Depth {depth} | Updated Beta at Node {node_index}: {beta}")
            if beta <= alpha:
                print(f"{indent}Depth {depth} | Pruning at Node {node_index} | Beta: {beta} <= Alpha: {alpha}")
                break
        return min_eval

if __name__ == "__main__":
    print("Enter 8 leaf node values (separated by space):")
    values = list(map(int, input().split()))
    if len(values) != 8:
        print("Error: You must provide exactly 8 leaf node values.")
    else:
        print("\nDetailed Alpha-Beta Pruning Process:\n")
        result = alpha_beta_pruning(0, 0, True, values, float('-inf'), float('inf'))
        print(f"\nThe optimal value is: {result}")
