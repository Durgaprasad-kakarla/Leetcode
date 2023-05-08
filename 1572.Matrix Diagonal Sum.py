class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m=len(mat)
        sum1=0
        for i in range(m):
            sum1+=mat[i][i]
            sum1+=mat[i][m-i-1]
        return sum1 if m%2==0 else sum1-mat[m//2][m//2]
''' Time Complexity--O(m)
    Space Complexity--O(1)'''
