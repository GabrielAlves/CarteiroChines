class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.quant_vertices = len(grafo)

    def __str__(self):
        grafo = ""

        for i in range(self.quant_vertices):
            for j in range(self.quant_vertices):
                grafo += f"{self.grafo[i][j]}"

                if j != self.quant_vertices - 1:
                    grafo += " "

            if i != self.quant_vertices - 1:
                grafo += "\n"

        return grafo