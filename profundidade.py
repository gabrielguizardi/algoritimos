def pop (array):
  return array.pop()
  
def push (stack, element):
  return stack.append(element)

def insert_vertex (fork, vertex, adjacent_vertex):
  if vertex not in fork:
    fork[vertex] = []

  if adjacent_vertex not in fork:
    fork[adjacent_vertex] = []

  fork[vertex].append(adjacent_vertex)
  fork[adjacent_vertex].append(vertex)
  
def build_a_fork ():
  fork = {}

  while True:
    input_fork_value = input('Digite o nome do vertíce para continuar ou Fim para parar: ')

    if (input_fork_value.upper() == 'FIM'):
      break

    input_adjacent_value = input('Digite o vertíce adjacente: ')
    insert_vertex(fork, input_fork_value, input_adjacent_value)

  return fork

def dfs ():
  fork = build_a_fork()
  visited = []
  stack = []

  for vertex in fork.keys():
    if vertex not in visited:
      visited.append(vertex)

    for adjacent_vertex in fork[vertex]:
      if adjacent_vertex not in visited:
        visited.append(adjacent_vertex)
  print(visited)
  
        


dfs()