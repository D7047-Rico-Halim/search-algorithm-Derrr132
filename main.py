from graphs import bfs, dfs, ucs, greedy_bfs, a_star

# main.py

# Declare the graph as an adjacency list with edge weights
graph = {
    'A' : [('B',1), ('C',4)],
    'B' : [('C',2), ('D',5)],
    'C' : [('D',1), ('E',3)],
    'D' : [('F',2)],
    'E' : [('F',1)],
    'F' : [('G',3)]   
}

for node in graph:
    print(f"Node {node} terhubung ke:")
    for neighbor, weight in graph[node]:
        print(f"- Node {neighbor} dengan bobot {weight}")


# Declare the heuristic values for each node
heuristics = {
    'A' : 7,
    'B' : 6,
    'C' : 4,
    'D' : 3,
    'E' : 2,
    'F' : 1,
    'G' : 0
}

for node in heuristics :
    print(f"Node {node} memiliki heuristic value {heuristics[node]}")
