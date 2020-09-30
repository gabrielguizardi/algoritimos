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

def buscar_por_largura(grafo, vertice_inicial):
  visitados = [vertice_inicial]
  fila = [vertice_inicial]

  while fila:
    vertice = fila.pop(0) # atribui e remove o primeiro vertice da fila

    for vertice_adjacente in grafo[vertice]:
      if vertice_adjacente not in visitados:
        visitados.append(vertice_adjacente)
        fila.append(vertice_adjacente)
  
  return visitados

print(buscar_por_largura(grafo, 'A'))
