grafo = {
  'A': set(['B', 'J']),
  'B': set(['A', 'D', 'I']),
  'J': set(['A', 'I', 'C']),
  'D': set(['B', 'C', 'I', 'E', 'H']),
  'I': set(['B', 'J', 'D']),
  'C': set(['J', 'D']),
  'E': set(['D', 'F']),
  'H': set(['D', 'G']),
  'F': set(['E', 'G']),
  'G': set(['H', 'F'])
}

def buscar_por_profundidade(grafo, vertice, visitado_aleatorio=set(), visitado_nao_aleatorio=[]):
  visitado_aleatorio.add(vertice)
  visitado_nao_aleatorio.append(vertice)

  for vertice_adjacente in grafo[vertice]:
    if vertice_adjacente not in visitado_aleatorio:
      buscar_por_profundidade(grafo, vertice_adjacente, visitado_aleatorio, visitado_nao_aleatorio)
  return visitado_nao_aleatorio

resultado = buscar_por_profundidade(grafo, 'A')

print(f"Resultado do busca: {resultado}")