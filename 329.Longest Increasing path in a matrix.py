class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[-1 for i in range(n)]for j in range(m)]
        def check(matrix,i,j,dp,parent):
            m=len(matrix)
            n=len(matrix[0])
            if i<0 or j<0 or i>=m or j>=n or matrix[i][j]<=parent:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=1+check(matrix,i-1,j,dp,matrix[i][j])
            down=1+check(matrix,i+1,j,dp,matrix[i][j])
            left=1+check(matrix,i,j-1,dp,matrix[i][j])
            right=1+check(matrix,i,j+1,dp,matrix[i][j])
            dp[i][j]=max(up,down,left,right)
            return dp[i][j]
        for i in range(m):
            for j in range(n):
                if dp[i][j]==-1:
                    check(matrix,i,j,dp,-1)
        maxlen=0
        for i in range(m):
            for j in range(n):
                maxlen=max(maxlen,dp[i][j])
        return maxlen
''' Time complexity--O(m*n)
    Space Complexity--O(m*n)'''
