
#Definindo e imprimindo na tela Grafo  com lista e/ou matriz de adjacencia.

''' 

A funcao recebe como parametros uma lista - tipo de dado - de vertices (nós) e arestas - tipo lista, data type. Basta utilizá-la no
'if' onde está disciplimando o __name__ == '__main__'. Neste bloco se define como a área do código em que toda a função deve rodar.


 haverá, na definição abaixo, um código em que 
'''


#Definindo funcao que cria grafo e o percorre retornando-o.

def cria_grafo_lista_adjacencia(lista_vertices, lista_arestas):
    grafo = {}
    for vertice in lista_vertices:
        grafo[vertice] = []
    for aresta in lista_arestas:
        grafo[aresta[0]].append(aresta[1])
    return grafo



if __name__ == "__main__":
  
    lista_vertices = ['a', 'b', 'c', 'd']
    lista_arestas = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b')]
    grafo = cria_grafo_lista_adjacencia(lista_vertices, lista_arestas)
    print(grafo)
