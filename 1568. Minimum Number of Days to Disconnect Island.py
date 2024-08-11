class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def dfs(row,col,grid,vis):
            global count
            n,m=len(grid),len(grid[0])
            vis[row][col]=1
            count+=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and not vis[nrow][ncol]:
                    dfs(nrow,ncol,grid,vis)
        cnt=0
        vis=[[0 for i in range(m)] for j in range(n)]
        global count
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    dfs(i,j,grid,vis)
                    cnt+=1
        if cnt>1 or cnt==0:
            return 0
        tot=count
        for i in range(n):
            for j in range(m):
                if vis[i][j]==1:
                    grid[i][j]=0
                    new_vis=[[0 for i in range(m)] for j in range(n)]
                    dr=[-1,0,1,0]
                    dc=[0,-1,0,1]
                    count=0
                    for x in range(4):
                        nrow=i+dr[x]
                        ncol=j+dc[x]
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1:
                            dfs(nrow,ncol,grid,new_vis)
                            break
                    if count==0 or count!=tot-1:
                        return 1
                    grid[i][j]=1
        return 2
''' Time Complexity--O(m*m*n*n)
    Space Complexity--O(m*n)'''
