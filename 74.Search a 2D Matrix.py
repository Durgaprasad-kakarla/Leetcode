class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        x=len(matrix[0])
        for i in range(n):
            if matrix[i][x-1]>=target:
                for j in range(x):
                    if matrix[i][j]==target:
                        return True
        return False
''' Time Complexity--O(m*n)
    Space Complexity--O(1)'''
