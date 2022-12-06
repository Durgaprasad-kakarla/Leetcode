import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #Firstly convert matrix into the transpose of the matrix
        for i in range(n):
            for j in range(i):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(n):#reverse the columns of the matrix
            matrix[i]=matrix[i][::-1]
       
        
