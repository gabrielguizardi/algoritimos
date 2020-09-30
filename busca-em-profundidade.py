def dfs(graph, start, visited=None):
  if visited is None:
    visited = set()
    print(start)
  visited.add(start)

  for next in graph[start]:
    if next not in visited:
      print(next)
      dfs(graph, next, visited)
  return visited

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

dfs(graph, 'A')