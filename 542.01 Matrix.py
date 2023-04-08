class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        vis=[[0 for  i in range(m)] for j in range(n)]
        dist=[[0 for i in range(m)] for j in range(n)]
        queue=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append([[i,j],0])
                    vis[i][j]=1
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while queue:
            x=queue.pop(0)
            row=x[0][0]
            col=x[0][1]
            steps=x[1]
            dist[row][col]=steps
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and ncol>=0 and nrow<n and ncol<m and not vis[nrow][ncol]:
                    vis[nrow][ncol]=1
                    queue.append([[nrow,ncol],steps+1])
        return dist
 ''' Time Complexity--O(n^2)
     Space Complexity--O(n^2)'''
