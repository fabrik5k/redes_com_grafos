# Função main para testar a classe Digrafo
import Grafo

if __name__ == '__main__':
    # Cria um digrafo com 5 vértices
    digrafo = Grafo.Digrafo(6)

    # Adiciona algumas arestas e seus respectivos pesos
    # digrafo.adicionar_aresta(0, 1, 3)
    # digrafo.adicionar_aresta(0, 2, 5)
    # digrafo.adicionar_aresta(1, 3, 1)
    # digrafo.adicionar_aresta(3, 4, 2)
    # digrafo.adicionar_aresta(4, 0, 8)

    #A: 0
    #B: 1
    #C: 2
    #D: 3

    digrafo.adicionar_aresta(0, 1, 2)
    digrafo.adicionar_aresta(1, 2, 5)
    digrafo.adicionar_aresta(2, 3, 3)
    digrafo.adicionar_aresta(3, 4, 4)
    digrafo.adicionar_aresta(4, 5, 7)
    digrafo.adicionar_aresta(5, 0, 2)
    digrafo.adicionar_aresta(0, 2, 5)
    digrafo.adicionar_aresta(0, 3, 2)
    digrafo.adicionar_aresta(0, 4, 2)
    digrafo.adicionar_aresta(1, 3, 8)
    digrafo.adicionar_aresta(1, 4, 4)
    digrafo.adicionar_aresta(1, 5, 9)
    digrafo.adicionar_aresta(2, 4, 2)
    digrafo.adicionar_aresta(2, 5, 6)
    digrafo.adicionar_aresta(3, 5, 5)

    # Exibe a matriz de adjacência do digrafo
    print("Matriz de Adjacência:")


    digrafo.floyd_warshall()

