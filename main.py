from grafo import Grafo
from carteiro_chines import CarteiroChines
from constantes import GRAFO_DE_ENTRADA

def main():
    grafo = Grafo(GRAFO_DE_ENTRADA)
    cc = CarteiroChines(grafo)
    peso_total = cc.resolver_carteiro_chines()
	
    print(f"Peso total do grafo usando algorítimo para resolver Carteiro Chinês:{peso_total}")
    

if __name__ == "__main__":
    main()