class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        m=len(mat)
        n=len(mat[0])
        mat=[[int(mat[j][i]) for i in range(n)] for j in range(m)]
        total=0
        max_square=0
        for i in range(m):
            max_square=max(mat[i][0],max_square)
        for i in range(1,n):
            max_square=max(mat[0][i],max_square)
        for i in range(1,m):
            for j in range(1,n):
                max_square=max(mat[i][j],max_square)
                if (not mat[i][j]) or (not mat[i-1][j]) or (not mat[i][j-1]) or (not mat[i-1][j-1]):
                    continue
                if mat[i][j] and mat[i-1][j] and mat[i][j-1] and mat[i-1][j-1]:
                    if mat[i-1][j]==mat[i][j-1]:
                        mat[i][j]=1+min(mat[i-1][j],mat[i-1][j-1])
                    else:
                        mat[i][j]=1+min(mat[i-1][j],mat[i][j-1])
                max_square=max(mat[i][j],max_square)
        return max_square*max_square
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
