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

def bfs(tree, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbour in tree.get(node, []):
                if neighbour not in visited:
                    queue.append(neighbour)
    return visited

def prettyPrint(visited):
    print("Traversal order:")
    for node in visited:
        print(node, end=" ")
    print()

prettyPrint(bfs(tree, start))
