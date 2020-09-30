import random

def insere_aresta(grafo, a, b):
  if a not in grafo:
    grafo[a] = []
  if b not in grafo:
    grafo[b] = []
  grafo[a].append(b)
  grafo[b].append(a)

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

  return largura, pai, aresta, nivel

grafo = {
  'A': ['B', 'J'],
  'B': ['A', 'D', 'I'],
  'J': ['A', 'I', 'C'],
  'D': ['B', 'C', 'I', 'E', 'H'],
  'I': ['B', 'J', 'D'],
  'C': ['J', 'D'],
  'E': ['D', 'F'],
  'H': ['D', 'G'],
  'F': ['E', 'G'],
  'G': ['H', 'F']
}

largura, pai, aresta, nivel = busca_em_largura(grafo, 'A')

print(list(largura.keys()))
    for vizinho in grafo.get(vertice):

      if not largura.get(vizinho): 
        fila.append(vizinho) 
        l += 1 
        largura[vizinho] = l
        pai[vizinho] = vertice
        nivel[vizinho] = nivel[vertice] + 1

  return largura, pai, aresta, nivel

grafo = {
  'A': ['B', 'J'],
  'B': ['A', 'D', 'I'],
  'J': ['A', 'I', 'C'],
  'D': ['B', 'C', 'I', 'E', 'H'],
  'I': ['B', 'J', 'D'],
  'C': ['J', 'D'],
  'E': ['D', 'F'],
  'H': ['D', 'G'],
  'F': ['E', 'G'],
  'G': ['H', 'F']
}

largura, pai, aresta, nivel = busca_em_largura(grafo, 'A')

print(list(largura.keys()))
    for vizinho in grafo.get(vertice):

      if not largura.get(vizinho): 
        fila.append(vizinho) 
        l += 1 
        largura[vizinho] = l
        pai[vizinho] = vertice
        nivel[vizinho] = nivel[vertice] + 1

  return largura, pai, aresta, nivel

grafo = {
  'A': ['B', 'J'],
  'B': ['A', 'D', 'I'],
  'J': ['A', 'I', 'C'],
  'D': ['B', 'C', 'I', 'E', 'H'],
  'I': ['B', 'J', 'D'],
  'C': ['J', 'D'],
  'E': ['D', 'F'],
  'H': ['D', 'G'],
  'F': ['E', 'G'],
  'G': ['H', 'F']
}

largura, pai, aresta, nivel = busca_em_largura(grafo, 'A')

print(list(largura.keys()))
    for vizinho in grafo.get(vertice):

      if not largura.get(vizinho): 
        fila.append(vizinho) 
        l += 1 
        largura[vizinho] = l
        pai[vizinho] = vertice
        nivel[vizinho] = nivel[vertice] + 1

  return largura, pai, aresta, nivel

grafo = {
  'A': ['B', 'J'],
  'B': ['A', 'D', 'I'],
  'J': ['A', 'I', 'C'],
  'D': ['B', 'C', 'I', 'E', 'H'],
  'I': ['B', 'J', 'D'],
  'C': ['J', 'D'],
  'E': ['D', 'F'],
  'H': ['D', 'G'],
  'F': ['E', 'G'],
  'G': ['H', 'F']
}

largura, pai, aresta, nivel = busca_em_largura(grafo, 'A')

print(list(largura.keys()))
