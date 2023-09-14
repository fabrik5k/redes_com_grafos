class Digrafo:
    def __init__(self, num_vertices):
        # Inicializa a matriz de adjacência com zeros
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        # Define o número total de vértices do digrafo
        self.num_vertices = num_vertices

    def adicionar_aresta(self, origem, destino, peso=1):
        # Verifica se os vértices são válidos
        if origem >= self.num_vertices or destino >= self.num_vertices or origem < 0 or destino < 0:
            print("Vértice não existe!")
            return
        # Adiciona o peso na matriz de adjacência na posição de origem e destino
        self.matriz_adjacencia[origem][destino] += peso

    def exibir(self):
        # Imprime cada linha da matriz de adjacência
        for linha in self.matriz_adjacencia:
            print(linha)

    def possui_loops(self):
        # Lista para armazenar os vértices com loops
        vertices_com_loops = []
        # Verifica se existe algum loop nos vértices
        for i in range(self.num_vertices):
            if self.matriz_adjacencia[i][i] != 0:
                vertices_com_loops.append(i)
        # Exibe resultado
        if not vertices_com_loops:
            print("Não possui loops.")
        else:
            print("Loops nos vértices:", vertices_com_loops)

    def possui_arestas_paralelas(self):
        # Lista para armazenar os pares de vértices com arestas paralelas
        vertices_com_paralelas = []
        # Verifica se existem arestas paralelas
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i != j and self.matriz_adjacencia[i][j] > 1:
                    vertices_com_paralelas.append((i, j))
        # Exibe resultado
        if not vertices_com_paralelas:
            print("Não possui arestas paralelas.")
        else:
            print("Arestas paralelas entre os vértices:", vertices_com_paralelas)

    def grau_entrada(self, v=None):
        if v == None:
            return [sum([self.matriz_adjacencia[i][v] for i in range(self.num_vertices)]) for v in range(self.num_vertices)]
        elif v >= 0 and v < self.num_vertices:
            return sum([self.matriz_adjacencia[i][v] for i in range(self.num_vertices)])
        else:
            print("Vértice não existe!")
            return None

    def grau_saida(self, v=None):
        if v == None:
            return [sum(self.matriz_adjacencia[i]) for i in range(self.num_vertices)]
        elif v >= 0 and v < self.num_vertices:
            return sum(self.matriz_adjacencia[v])
        else:
            print("Vértice não existe!")
            return None

    def floyd_warshall(self):
        # Inicializa a matriz de distâncias com infinito em todas as posições,
        # exceto na diagonal principal onde os valores são zero

        print("\n-----------------------------\nAlgoritmo de Floyd-Warshall:\n")

        dist = [[float('inf')] * self.num_vertices for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            dist[i][i] = 0  # A distância de um vértice a ele mesmo é sempre 0

            # Preenche a matriz de distâncias com os pesos das arestas existentes
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    dist[i][j] = self.matriz_adjacencia[i][j]

        print("Matriz de Distância:\n")
        for linha in dist:
          print(linha)
        print("\n")

        # Atualiza a matriz de distâncias usando o algoritmo de Floyd-Warshall
        # k é o vértice intermediário, i é o vértice de origem, e j é o vértice de destino
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    # Se o caminho através do vértice k for mais curto, atualiza dist[i][j]
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

            print("Matriz",k,":\n")
            for linha in dist:
              print(linha)
            print("\n")

        # Exibe a matriz de distâncias mais curtas entre todos os pares de vértices
        print("\n-----------------------------\nMatriz de Distâncias Mais Curtas (Floyd-Warshall):\n")
        for linha in dist:
            print(linha)

        print("\n")
        # Retorna a matriz de distâncias mais curtas
        return dist

    def encontrar_caminho(self, origem, destino):
        if origem < 0 or origem >= self.num_vertices or destino < 0 or destino >= self.num_vertices:
            print("Vértice de origem ou destino inválido!")
            return None, None

        distancias = self.floyd_warshall()

        if distancias[origem][destino] == float('inf'):
            print("Não há caminho entre a origem e o destino.")
            return None, None

        peso_total = 0

        caminho = [origem]
        while origem != destino:
            for i in range(self.num_vertices):
                if distancias[origem][destino] == distancias[i][destino] + self.matriz_adjacencia[origem][i]:
                    peso_total += self.matriz_adjacencia[origem][i]
                    origem = i
                    caminho.append(origem)

        return caminho, peso_total

