def busca_em_largura(grafo, vertice_do_grafo):
  fila = [] 

  visitados = {}
  l = 1 
  pai = {} 
  nivel = {} 
  aresta = {} 

  fila.append(vertice_do_grafo)
  visitados[vertice_do_grafo] = l
  pai[vertice_do_grafo] = None
  nivel[vertice_do_grafo] = 1

  while len(fila):
    vertice = fila.pop(0) 

    for vizinho in grafo.get(vertice):
      if not visitados.get(vizinho): 
        fila.append(vizinho) 
        l += 1 
        visitados[vizinho] = l
        pai[vizinho] = vertice
        nivel[vizinho] = nivel[vertice] + 1

  return visitados

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

visitados = busca_em_largura(grafo, 'A')

print(list(visitados.keys()))
