class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=[]
        n=len(grid)
        m=len(grid[0])
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        queue.append([[0,0],1])
        vis=[[0 for i in range(m)]for i in range(n)]
        delrow=[1,1,1,0,-1,-1,-1,0]
        delcol=[1,0,-1,1,1,0,-1,-1]
        while queue:
            x=queue.pop(0)
            row=x[0][0]
            col=x[0][1]
            steps=x[1]
            if row==n-1 and col==m-1:
                return steps
            for i in range(8):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and grid[nrow][ncol]==0:
                    vis[nrow][ncol]=1
                    queue.append([[nrow,ncol],steps+1])
        return -1
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
