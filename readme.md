# CarteiroChines

Implementação de algorítmo para o problema do carteiro chinês em grafos não orientados. Foi parte de um trabalho da disciplina de grafos. Apenas modulei o que eu tinha escrito antes. Basicamente calcula o peso de um ciclo euleriano. 

Se o grafo possuir vértices ímpares, o algorítmo:

1. Lista todas as arestas que podem ser formadas combinando os vértices ímpares. Calcula para cada par de vértices, a distância mínima entre eles usando o algorítmo de dijkstra.
2. Ordena todas essas arestas com base nas distâncias entre os vértices;
3. Determina o conjunto de emparelhamento entre essas arestas. Esse conjunto contém as menores arestas que são necessárias acrescentar para realizar o ciclo euleriano do grafo.
4. Acrescenta o peso dessas arestas duplicadas na contagem total do peso.