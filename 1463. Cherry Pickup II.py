class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def func(i,j,i1,j1,dp):
            m=len(grid)
            n=len(grid[0])
            if i<0 or j<0 or i1<0 or j1<0 or i==m or i1==m or j==n or j1==n:
                return -float('inf')
            if i==m-1 and i1==m-1:
                if j==j1 and i==i1:
                    return grid[i][j]
                return grid[i][j]+grid[i1][j1]
            if dp[i][j][i1][j1]!=-1:
                return dp[i][j][i1][j1]
            if i==i1 and j==j1:
                a=func(i+1,j,i1+1,j1,dp)+grid[i][j]
                a1=func(i+1,j,i1+1,j1+1,dp)+grid[i][j]
                a2=func(i+1,j,i1+1,j1-1,dp)+grid[i][j]
                b=func(i+1,j+1,i1+1,j1,dp)+grid[i][j]
                b1=func(i+1,j+1,i1+1,j1+1,dp)+grid[i][j]
                b2=func(i+1,j+1,i1+1,j1-1,dp)+grid[i][j]
                c=func(i+1,j-1,i1+1,j1,dp)+grid[i][j]
                c1=func(i+1,j-1,i1+1,j1+1,dp)+grid[i][j]
                c2=func(i+1,j-1,i1+1,j1-1,dp)+grid[i][j]
                dp[i][j][i1][j1]=max(a,a1,a2,b,b1,b2,c,c1,c2)
                return max(a,a1,a2,b,b1,b2,c,c1,c2)
            else:
                a=func(i+1,j,i1+1,j1,dp)+grid[i][j]+grid[i1][j1]
                a1=func(i+1,j,i1+1,j1+1,dp)+grid[i][j]+grid[i1][j1]
                a2=func(i+1,j,i1+1,j1-1,dp)+grid[i][j]+grid[i1][j1]
                b=func(i+1,j+1,i1+1,j1,dp)+grid[i][j]+grid[i1][j1]
                b1=func(i+1,j+1,i1+1,j1+1,dp)+grid[i][j]+grid[i1][j1]
                b2=func(i+1,j+1,i1+1,j1-1,dp)+grid[i][j]+grid[i1][j1]
                c=func(i+1,j-1,i1+1,j1,dp)+grid[i][j]+grid[i1][j1]
                c1=func(i+1,j-1,i1+1,j1+1,dp)+grid[i][j]+grid[i1][j1]
                c2=func(i+1,j-1,i1+1,j1-1,dp)+grid[i][j]+grid[i1][j1]
                dp[i][j][i1][j1]=max(a,a1,a2,b,b1,b2,c,c1,c2)
                return max(a,a1,a2,b,b1,b2,c,c1,c2)
        m=len(grid)
        n=len(grid[0])
        dp=[[[[-1 for i in range(n)]for j in range(m)]for k in range(n)]for x in range(m)]
        return func(0,0,0,len(grid[0])-1,dp)
''' Time Complexity--O(m^2*n^2)
    Space Complexity--O(m^2*n^2)'''
