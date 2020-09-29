import random

def insere_aresta(grafo, a, b):
    if a not in grafo:
        grafo[a] = []
    if b not in grafo:
        grafo[b] = []
    grafo[a].append(b)
    grafo[b].append(a)

grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x == 'FIM':
        break
    y = input("Entre com um vertice adjacente:")

    insere_aresta(grafo, x, y)

def busca_em_largura(grafo, vertice_do_grafo):
    fila = [] 

    largura = {}
    l = 1 
    pai = {} 
    nivel = {} 
    aresta = {} 

    fila.append(vertice_do_grafo)
    largura[vertice_do_grafo] = l
    pai[vertice_do_grafo] = None
    nivel[vertice_do_grafo] = 1

    while len(fila):
        vertice = fila.pop(0) 

        for vizinho in grafo.get(vertice):

            if not largura.get(vizinho): 
                fila.append(vizinho) 
                l += 1 
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1 

            print(f"{vertice} => {vizinho}")

    return largura, pai, aresta, nivel

largura, pai, aresta, nivel = busca_em_largura(grafo, list(grafo.keys())[random.randint(0, len(grafo))])
