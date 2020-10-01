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

def buscar_por_profundidade(grafo, vertice_inicial):
  pilha = [vertice_inicial] 
  visitados = []

  while pilha:
    vertice_atual = pilha.pop()

    if vertice_atual in visitados:
      continue

    visitados.append(vertice_atual)

    for adjacente in grafo[vertice_atual]:
      pilha.append(adjacente)

  return visitados

resultado = buscar_por_profundidade(grafo, 'A')

print(f"Resultado do busca: {resultado}")