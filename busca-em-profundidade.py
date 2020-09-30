
graph = {
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

def dfs(graph, start, visited=None, not_random_list=[]):
  if visited is None:
    visited = set()
  visited.add(start)
  not_random_list.append(start)

  for next in graph[start]:
    if next not in visited:
      dfs(graph, next, visited, not_random_list)
  return not_random_list

result = dfs(graph, 'A')

print(f"Resultado do busca: {result}")