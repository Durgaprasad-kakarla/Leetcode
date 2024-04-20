class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n,m=len(land),len(land[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        def bfs(row,col,land):
            queue=deque()
            queue.append([row,col])
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            while queue:
                row,col=queue.popleft()
                for i in range(4):
                    nrow=row+dr[i]
                    ncol=col+dc[i]
                    if nrow>=0 and ncol>=0 and nrow<n and ncol<m and not vis[nrow][ncol] and land[nrow][ncol]==1:
                        queue.append([nrow,ncol])
                        vis[nrow][ncol]=1 
            return [row,col]
        groups=[]
        for i in range(n):
            for j in range(m):
                if land[i][j]==1 and not vis[i][j]:
                    last_row,last_col=bfs(i,j,land)
                    groups.append([i,j,last_row,last_col])
        return groups
''' Time Complexity--O(n*m)
    Space Complexity--O(n*m)'''
