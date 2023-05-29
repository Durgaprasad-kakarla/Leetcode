class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set1=set()
        set2=set()
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    set1.add(i)
                    set2.add(j)
        for i in range(n):
            for j in range(m):
                if i in set1 or j in set2:
                    matrix[i][j]=0
''' Time Complexity--O(2*m*n)
    Space Complexity--O(m)+O(n)'''
