

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def es_l_lindo(s,n):
  l = letras[n]
  if (s[0] == l):
    return 0
  else:
    return 1


def dividir(s,medio):
  subproblema1 = s[:medio]
  subproblema2 = s[medio:]
  return subproblema1, subproblema2



def contarCaracteresCorrectos(s,n):
  contador = 0
  l = letras[n]
  for i in range(len(s)):
    if (s[i] == l):
      contador += 1
  return contador


def divideAndConquer(s,n):
  #Caso base:
  if (len(s)==1):
    return es_l_lindo(s,n)

  #dividir
  medio = len(s)//2
  subproblema1, subproblema2 = dividir(s,medio)

  #ContarCambios
  contadorIzquierda = medio - contarCaracteresCorrectos(subproblema1,n)
  contadorDerecha = medio - contarCaracteresCorrectos(subproblema2,n)

  #Conquistar
  siVoyPorIzquierda = divideAndConquer(subproblema1,n+1)
  siVoyPorDerecha = divideAndConquer(subproblema2,n+1)


  # Unir las soluciones parciale.
  solucion_parcial1 = siVoyPorDerecha + contadorIzquierda
  solucion_parcial2 = siVoyPorIzquierda + contadorDerecha

  res = min(solucion_parcial1, solucion_parcial2)
  return res


def a_lindo(s):
  return divideAndConquer(s,0)


import sys
t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  s = sys.stdin.readline().strip()
  resultado = a_lindo(s)
  print(resultado)


