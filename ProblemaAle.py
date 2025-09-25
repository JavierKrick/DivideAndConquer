#Si lo planteo como que quiero encontrar el valor en la posición k, se parece muchpisimo a búsquda binaria
import sys

"""
                          10
                  5        0         5
              2   1   2    0    2    1    2
          1   1  1  1  1  0  1   1  1  1   1


  Me fijo el último padre en comun.

"""




def largonDeLaSecuencia(n):
  if n < 2:
    return 1
  else:
    return largonDeLaSecuencia(n//2)*2 + 1



def busquedaBinaria(n,k,largo):
  medio = largo // 2 + 1

  if (k == medio):
    return n % 2
  elif (k < medio):
    return busquedaBinaria(n//2, k,medio-1)
  else:
    return busquedaBinaria(n//2, k - medio,medio-1)


def UltimoPadreEnComun(n,l,r):
  largo = largonDeLaSecuencia(n)
  n,l,r,mid,largo = ultimo_padre_en_comun(n,l,r,largo)
  return n,l,r, mid,largo


def ultimo_padre_en_comun(n, l, r,largo):
  if l > r:
    l, r = r, l
    
  if n == 0 or n == 1:
    return n
  

  largoRama = largonDeLaSecuencia(n // 2)
  mid = largoRama + 1
  if ((r < mid and l < mid)):
    return ultimo_padre_en_comun(n // 2, l, r,mid-1)
  elif ((r > mid and l > mid)):
    return ultimo_padre_en_comun(n // 2, l-mid, r-mid,mid-1)
  else:
    return n, l, r, mid,largo


"""
                        10
                5        0         5
            2   1   2    0    2    1    2
         1  0 1 1 1 0 1  1  1 0 1  1  1 0  1


Me fijo el último padre en comun.

"""



def UnirResultados(n,l,r):
  # sería f(n) + n mod 2 + f(n)
  # Pero solo hay overlap en una parte
  # Elementos de overlap*2 + elementos no de overlap + n mod 2


  #actualizo los valores

  if l == r:
    largo = largonDeLaSecuencia(n)
    return busquedaBinaria(n,l,largo)




  n,l,r,mid,largo = UltimoPadreEnComun(n,l,r)
  
  nMOd2 = n % 2

  haciaIzq = mid-l
  haciaDer = r-mid
  
  overlap = min(haciaIzq,haciaDer)
  sinOverlapHasta = max(haciaIzq,haciaDer)


  sumaOverlap = 0
  for k in range (1,overlap+1):
    sumaOverlap = sumaOverlap + busquedaBinaria(n,k,largo)
  
  sumaSinOverlap = 0
  for k in range (overlap+1, sinOverlapHasta+1):
    sumaSinOverlap = sumaSinOverlap + busquedaBinaria(n,k,largo)

  res =  sumaOverlap*2 + sumaSinOverlap + nMOd2
  
  return res

"""
                    6
              3     0     3
           1  1  1  0  1  1  1
"""



n, l, r = map(int, sys.stdin.readline().split())
print(UnirResultados(n, l, r))





