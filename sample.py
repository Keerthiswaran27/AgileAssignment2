n = int(input("enter number of nodes: "))
print("enter the adjacency matrix ka nodes:") 
labels = input().split()

graph = {node : [] for node in labels}
m=int(input("enter number of edges: "))
print("enter the edges:")
for _ in range(m):
    u, v = input().split()
    graph[u].append(v)

for node in graph:
    print(f"{node} -> {' -> '.join(graph[node])}")()
for i in range(n): 
    for j in range(n): 
        print(graph[i][j], end = " ") 
    print()

