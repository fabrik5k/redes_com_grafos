import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def warshall(adj_matrix):
    n = len(adj_matrix)
    R = adj_matrix.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])

    return R

def plot_graph(matrix):
    G = nx.DiGraph()

    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2, edge_color="gray", arrowsize=20)
    plt.show()

# Exemplo: Matriz de adjacência de um digrafo
adj_matrix = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
])

closure_matrix = warshall(adj_matrix)
plot_graph(closure_matrix)
