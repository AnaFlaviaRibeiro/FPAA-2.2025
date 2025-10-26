import networkx as nx
import matplotlib.pyplot as plt
import random
from datetime import datetime

class Grafo:
    def __init__(self, qtd_vertices, eh_direcionado=False):
        """
        Constrói um grafo com matriz de adjacência e cria arestas aleatórias.

        Parâmetros:
            qtd_vertices (int): Quantidade de vértices do grafo.
            eh_direcionado (bool): Define se o grafo é direcionado (True) ou não (False).
        """
        self.num_vertices = qtd_vertices
        self.direcionado = eh_direcionado
        self.matriz_adj = [[0] * qtd_vertices for _ in range(qtd_vertices)]
        self._criar_grafo_aleatorio()

    def _criar_grafo_aleatorio(self):
        """Gera um grafo aleatório válido e não repetido."""
        random.seed(datetime.now().timestamp())  # Semente variável

        # Define número mínimo e máximo de arestas
        minimo_arestas = self.num_vertices - 1
        max_arestas = (
            self.num_vertices * (self.num_vertices - 1)
            if self.direcionado
            else self.num_vertices * (self.num_vertices - 1) // 2
        )
        total_arestas = random.randint(minimo_arestas, max_arestas)

        # Lista com todas as possíveis conexões entre vértices
        arestas_possiveis = []
        for origem in range(self.num_vertices):
            for destino in range(self.num_vertices):
                if origem != destino and (self.direcionado or origem < destino):
                    arestas_possiveis.append((origem, destino))

        # Seleciona aleatoriamente as arestas que serão usadas
        random.shuffle(arestas_possiveis)
        escolhidas = arestas_possiveis[:total_arestas]

        # Popula a matriz de adjacência
        for u, v in escolhidas:
            self.matriz_adj[u][v] = 1
            if not self.direcionado:
                self.matriz_adj[v][u] = 1

    def _pode_visitar(self, vertice, caminho, posicao):
        """Verifica se o vértice pode ser adicionado ao caminho atual."""
        if self.matriz_adj[caminho[posicao - 1]][vertice] == 0:
            return False
        if vertice in caminho:
            return False
        return True

    def _busca_hamiltoniana(self, caminho, posicao):
        """Executa a busca recursiva para encontrar o caminho Hamiltoniano."""
        if posicao == self.num_vertices:
            return True

        for vertice in range(self.num_vertices):
            if self._pode_visitar(vertice, caminho, posicao):
                caminho[posicao] = vertice
                if self._busca_hamiltoniana(caminho, posicao + 1):
                    return True
                caminho[posicao] = -1  # backtracking

        return False

    def encontrar_caminho_hamiltoniano(self):
        """Procura um caminho Hamiltoniano no grafo."""
        for inicio in range(self.num_vertices):
            caminho = [-1] * self.num_vertices
            caminho[0] = inicio
            if self._busca_hamiltoniana(caminho, 1):
                return caminho
        return None

    def mostrar_grafo(self, caminho=None):
        """Desenha o grafo e destaca o caminho Hamiltoniano, se existir."""
        G = nx.DiGraph() if self.direcionado else nx.Graph()

        # Adiciona arestas
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adj[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color='skyblue',
            edge_color='gray',
            node_size=700,
            font_size=14,
            arrows=self.direcionado,
        )

        # Destaca caminho, se existir
        if caminho:
            conexoes = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=conexoes,
                edge_color='red',
                width=2,
                arrows=self.direcionado,
            )

        plt.title(f"Grafo {'Direcionado' if self.direcionado else 'Não Direcionado'}")
        plt.show()


if __name__ == "__main__":
    # Escolha de tipo de grafo
    eh_direcionado = input("Deseja grafo direcionado? (s/n): ").lower() == 's'

    # Número de vértices aleatório
    vertices = random.randint(5, 8)

    # Cria e analisa o grafo
    grafo = Grafo(vertices, eh_direcionado)
    caminho = grafo.encontrar_caminho_hamiltoniano()

    # Exibe o resultado
    if caminho:
        print(f"Caminho Hamiltoniano encontrado ({'direcionado' if eh_direcionado else 'não direcionado'}):")
        print(" → ".join(map(str, caminho)))
        grafo.mostrar_grafo(caminho)
    else:
        print(f"Nenhum caminho Hamiltoniano encontrado ({'direcionado' if eh_direcionado else 'não direcionado'}).")
        grafo.mostrar_grafo()
