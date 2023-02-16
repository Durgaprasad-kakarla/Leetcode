class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def fun(i,j,grid,dp):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 100000
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+fun(i-1,j,grid,dp)
            left=grid[i][j]+fun(i,j-1,grid,dp)
            dp[i][j]=min(up,left)
            return dp[i][j]
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for j in range(n)]for i in range(m)]
        return fun(m-1,n-1,grid,dp)

''' Time Complexity:O(m*n)------Space Complexity:O(m*n+(m-1)+(n-1))
