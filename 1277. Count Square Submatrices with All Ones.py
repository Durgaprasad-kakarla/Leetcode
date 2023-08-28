class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        new_mat=[[0 for i in range(n)] for j in range(m)]
        total=0
        for i in range(m):
            new_mat[i][0]=mat[i][0]
            total+=mat[i][0]
        for i in range(1,n):
            new_mat[0][i]=mat[0][i]
            total+=mat[0][i]
        for i in range(1,m):
            for j in range(1,n):
                if (not mat[i][j]) or (not new_mat[i-1][j]) or (not new_mat[i][j-1]) or (not new_mat[i-1][j-1]):
                    new_mat[i][j]=mat[i][j]
                if mat[i][j] and new_mat[i-1][j] and new_mat[i][j-1] and new_mat[i-1][j-1]:
                    if new_mat[i-1][j]==new_mat[i][j-1]:
                        new_mat[i][j]=1+min(new_mat[i-1][j],new_mat[i-1][j-1])
                    else:
                        new_mat[i][j]=1+min(new_mat[i-1][j],new_mat[i][j-1])
                total+=new_mat[i][j]
        return total
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
