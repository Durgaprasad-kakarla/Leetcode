class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def func(row,col,vis):
            if row<0 or row>=n or col<0 or col>=m:
                return 0
            if grid[row][col]==0 or vis[row][col]==1:
                return 0
            vis[row][col]=1
            dr=[0,-1,0,1]
            dc=[-1,0,1,0]
            maxi=0
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                maxi=max(grid[row][col]+func(nrow,ncol,vis),maxi)
            vis[row][col]=0
            return maxi
        maxi=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    vis=[[0 for i in range(m)] for j in range(n)]
                    maxi=max(maxi,func(i,j,vis))
        return maxi
''' Time Complexity--O((m*n)^2)
    Space Complexity--O(m*n)'''
