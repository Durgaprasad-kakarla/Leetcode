class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        def func(row,col):
            m=len(mat)
            n=len(mat[0])
            for j in range(n):
                if col!=j and mat[row][j]==1:
                    return False
            for i in range(m):
                if row!=i and mat[i][col]==1:
                    return False
            return True
        cnt=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and func(i,j):
                    cnt+=1
        return cnt
''' Time Complexity--O(m*n*max(m,n))
    Space Complexity--O(1)'''
