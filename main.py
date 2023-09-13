# Função main para testar a classe Digrafo
import Grafo

if __name__ == '__main__':
    # Cria um digrafo com 5 vértices
    digrafo = Grafo.Digrafo(4)

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

    digrafo.adicionar_aresta(0, 1, 3)
    digrafo.adicionar_aresta(1, 0, 8)
    digrafo.adicionar_aresta(2, 0, 5)
    digrafo.adicionar_aresta(0, 3, 7)
    digrafo.adicionar_aresta(3, 0, 2)
    digrafo.adicionar_aresta(1, 2, 2)
    digrafo.adicionar_aresta(2, 3, 1)

    # Exibe a matriz de adjacência do digrafo
    print("Matriz de Adjacência:")
    digrafo.exibir()

    # Verifica e exibe se o digrafo possui loops
    digrafo.possui_loops()

    # Verifica e exibe se o digrafo possui arestas paralelas
    digrafo.possui_arestas_paralelas()

    # Calcula e exibe os graus de entrada de todos os vértices
    print("Graus de entrada:", digrafo.grau_entrada())

    # Calcula e exibe os graus de saída de todos os vértices
    print("Graus de saída:", digrafo.grau_saida())

    # Executa o algoritmo de Floyd-Warshall e exibe a matriz de distâncias mais curtas
    digrafo.floyd_warshall()

