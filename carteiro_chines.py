from dijkstra import executar_dijkstra

class CarteiroChines:
    def __init__(self, grafo):
        self.grafo = grafo
        self.vertices_impares = []
        self.arestas_possiveis_entre_vertices_impares = []
        self.emparelhamento = []

    # Calcula o peso de um ciclo euleriano em um problema do formato "Carteiro Chinês"(inspeção de rotas)
    def resolver_carteiro_chines(self):
        peso_total = 0

        for vertice in range(self.grafo.quant_vertices):
            o_vertice_eh_impar = self.contar_grau_do_vertice(vertice) % 2 != 0

            if o_vertice_eh_impar:
                self.vertices_impares.append(vertice)
            
        # Passa por todas as arestas do grafo(sem repetições) e soma o peso no contador. Posições sem arestas não interferem no resultado(acrescentam 0)
        for i in range(self.grafo.quant_vertices - 1):
            for j in range(i + 1, self.grafo.quant_vertices):
                peso_total += self.grafo.grafo[i][j]
            
        # Se o grafo possuir vértices ímpares, então haverá arestas duplicadas. Os 3 métodos abaixo descobrem as menores arestas independentes formadas pelos vértices ímpares.
        if len(self.vertices_impares):
            self.listar_arestas_possiveis_entre_vertices_impares()
            self.ordenar_arestas_dos_vertices_impares()
            self.determinar_emparelhamento()

            # Acrescentar as arestas duplicadas pela etapa de emparelhamento na contagem do peso total
            for aresta in self.emparelhamento:
                peso_total += aresta[2]

        return peso_total                             
    
    def contar_grau_do_vertice(self, vertice):
        grau = 0
        
        for i in self.grafo.grafo[vertice]:
            if i > 0:
                grau += 1

        return grau

    def listar_arestas_possiveis_entre_vertices_impares(self):
        for i in range(len(self.vertices_impares) - 1):
            for j in range(i + 1, len(self.vertices_impares)):
                vertice_de_origem = self.vertices_impares[i]
                vertice_de_destino = self.vertices_impares[j]
                distancia_minima = executar_dijkstra(self.grafo, vertice_de_origem, vertice_de_destino)

                self.arestas_possiveis_entre_vertices_impares.append((vertice_de_origem, vertice_de_destino, distancia_minima))

    def ordenar_arestas_dos_vertices_impares(self):
        self.arestas_possiveis_entre_vertices_impares.sort(key = lambda x : x[2])

    def determinar_emparelhamento(self):
        self.emparelhamento.append(self.arestas_possiveis_entre_vertices_impares[0])
        vertice1 = self.arestas_possiveis_entre_vertices_impares[0][0]
        vertice2 = self.arestas_possiveis_entre_vertices_impares[0][1]
        vertices_incluidos = [vertice1, vertice2]

        for aresta in self.arestas_possiveis_entre_vertices_impares:
            vertice1 = aresta[0]
            vertice2 = aresta[1]

            if vertice1 not in vertices_incluidos and vertice2 not in vertices_incluidos:
                self.emparelhamento.append(aresta)
                vertices_incluidos.extend([vertice1, vertice2])