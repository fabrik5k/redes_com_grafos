# Função main para testar a classe Digrafo
import Grafo

if __name__ == '__main__':
    # Cria um digrafo com 6 vértices
    digrafo = Grafo.Digrafo(6)

    #A: 0
    #B: 1
    #C: 2
    #D: 3
    #E: 4
    #F: 5

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

    origem = int(input("Digite o vértice de origem (0-5): "))
    destino = int(input("Digite o vértice de destino (0-5): "))

    caminho, peso_total = digrafo.encontrar_caminho(origem, destino)
    if caminho:
        print(f"Caminho mais curto de {origem} para {destino}: {caminho}")
        print(f"Peso total do caminho: {peso_total}")

