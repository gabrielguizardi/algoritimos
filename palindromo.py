lista = []

def push(lista, topo, valor):
  lista.insert(topo, valor)

def pop(lista):
  lista.pop()

while True:
  palavra = input('Escreva uma palavra ou Fim para terminar: ')

  if (palavra.upper() == 'FIM'):
    break
  
  len_palavra = len(palavra)

  lista_letras = [] * len_palavra
  lista_letras_invertida = [] * len_palavra

  topo = 0

  for letra in palavra:
    push(lista_letras, topo, letra)

    topo += 1

  invertido = ''
  while topo > 0:
    topo -= 1
    invertido += lista_letras[topo]

    pop(lista_letras)
  
  print(f"Original: {palavra}")
  print(f"Invertido: {invertido}")
