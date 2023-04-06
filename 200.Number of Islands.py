class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        count=0
        def bfs(row,col,vis,grid):
            vis[row][col]=1
            queue=[]
            queue.append([row,col])
            while queue:
                x=queue.pop(0)
                row=x[0]
                col=x[1]
                delrow=[-1,0,1,0]
                delcol=[0,1,0,-1]
                for i in range(4):
                    nrow=row+delrow[i]
                    ncol=col+delcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=='1' and not vis[nrow][ncol]:
                        vis[nrow][ncol]=1
                        queue.append([nrow,ncol])
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col]=="1":
                    count+=1
                    bfs(row,col,vis,grid)
        print(vis)
        return count
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
