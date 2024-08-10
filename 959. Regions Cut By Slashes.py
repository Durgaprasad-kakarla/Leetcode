class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(row,col,grid):
            m,n=len(grid),len(grid[0])
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and ncol>=0 and nrow<m and ncol<n and grid[nrow][ncol]==0 and not vis[nrow][ncol]:
                    dfs(nrow,ncol,grid)
        m,n=len(grid),len(grid[0])
        new_grid=[[0 for i in range(n*3)] for j in range(m*3)]
        rows,cols=m*3,n*3
        for i in range(m):
            for j in range(n):
                r1,c1=i*3,j*3
                print(grid[i][j])
                if grid[i][j]=='/':
                    new_grid[r1][c1+2]=1
                    new_grid[r1+1][c1+1]=1
                    new_grid[r1+2][c1]=1
                elif grid[i][j]=='\\':
                    new_grid[r1][c1]=1
                    new_grid[r1+1][c1+1]=1
                    new_grid[r1+2][c1+2]=1
        vis=[[0 for i in range(cols)] for j in range(rows)]
        cnt=0
        for i in range(rows):
            for j in range(cols):
                if new_grid[i][j]==0 and not vis[i][j]:
                    dfs(i,j,new_grid)
                    cnt+=1
        return cnt
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
