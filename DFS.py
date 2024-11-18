print("Please enter the number of nodes: ")
n = int(input())
print("Please enter the start node: ")
start = input()
print("Please enter all the nodes (space-separated): ")
nodes = input().split()

tree = {}
for i in range(n):
    print(f"Please enter the nodes connected to {nodes[i]} (space-separated): ")
    tree[nodes[i]] = input().split()

visited = []

def dfs(node, tree, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in tree[node]:
            dfs(neighbour, tree, visited)

print("\nDFS Traversal Order:")
dfs(start, tree, visited)
