class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n)]for j in range(m)]
        def check(grid,i,j,dp,parent):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]<=parent:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=check(grid,i-1,j,dp,grid[i][j])
            down=check(grid,i+1,j,dp,grid[i][j])
            left=check(grid,i,j-1,dp,grid[i][j])
            right=check(grid,i,j+1,dp,grid[i][j])
            dp[i][j]=(up+left+down+right+1)%(10**9+7)
            return dp[i][j]
        for i in range(m):
            for j in range(n):
                if dp[i][j]==-1:
                    check(grid,i,j,dp,-1)
        sum=0
        print(dp)
        for i in range(m):
            for j in range(n):
                sum+=(dp[i][j])%(10**9+7)
        return sum%(10**9+7)
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
