from constantes import INFINITO

def executar_dijkstra(grafo, vertice_de_origem, vertice_de_destino):
    menores_distancias = [INFINITO] * grafo.quant_vertices
    menores_distancias[vertice_de_origem] = 0
    vertices_incluidos = [False] * grafo.quant_vertices

    for cout in range(grafo.quant_vertices):
        u = encontrar_vertice_mais_proximo_fora_dos_incluidos(grafo, menores_distancias, vertices_incluidos)

        vertices_incluidos[u] = True

        if u == vertice_de_destino:
            return menores_distancias[vertice_de_destino]

        for v in range(grafo.quant_vertices):
            if grafo.grafo[u][v] > 0 and vertices_incluidos[v] == False and menores_distancias[v] > menores_distancias[u] + grafo.grafo[u][v]:
                menores_distancias[v] = menores_distancias[u] + grafo.grafo[u][v]

def encontrar_vertice_mais_proximo_fora_dos_incluidos(grafo, menores_distancias, vertices_incluidos):
        min = INFINITO

        for v in range(grafo.quant_vertices):
            if menores_distancias[v] < min and vertices_incluidos[v] == False:
                min = menores_distancias[v]
                indice_minimo = v

        return indice_minimo