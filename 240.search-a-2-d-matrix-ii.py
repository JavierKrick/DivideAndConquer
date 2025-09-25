#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.BuscarEnMatriz(matrix,target,0,len(matrix[0])-1)

    


    def BuscarEnMatriz(self,matriz,target,alto,ancho):

        if alto == len(matriz) or ancho < 1:
            return False

        valor = matriz[alto][ancho]


        if valor == target:
            return True
        elif valor > target:
            return self.BuscarEnMatriz(matriz, target, alto, ancho-1)
        elif valor < target:
            return self.BuscarEnMatriz(matriz,target,alto+1,ancho)
        else:
            return False
        


        



            



        
# @lc code=end

