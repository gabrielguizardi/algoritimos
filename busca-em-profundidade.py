graph = {
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
  "e": ["f"],
  "f": []
}

def DFS(graph, start_node, stack = [], visited = []):
stack.append(start_node)

while stack:
  v = stack.pop()
  if v not in visited:
    visited.append(v)
    for neighbor in graph[v]:
      stack.append(neighbor)
      return visited

def dfs_get_connected_components_util(graph):
visited = []

for node in graph:
if node not in visited:
DFS_algo = DFS(graph, node)
print(DFS_algo)
visited = DFS_algo

print(dfs_get_connected_components_util(graph))