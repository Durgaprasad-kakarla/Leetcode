class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        queue=[]
        vis=[[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2 and not vis[i][j]:
                    queue.append([[i,j],0])
                    vis[i][j]=2
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        tm=0
        while queue:
            q=queue.pop(0)
            r=q[0][0]
            c=q[0][1]
            t=q[1]
            tm=max(tm,t)
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]!=2 and grid[nrow][ncol]==1:
                    queue.append([[nrow,ncol],t+1])
                    vis[nrow][ncol]=2
        for i in range(n):
            for j in range(m):
                if vis[i][j]!=2 and grid[i][j]==1:
                    return -1
        return tm
''' Time Complexity--O(n*m)
    Space Complexity--O(n*m)
