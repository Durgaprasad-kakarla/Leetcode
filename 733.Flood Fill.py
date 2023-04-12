class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(n,m,row,col,image,color,delrow,delcol,inicolor):
            image[row][col]=color
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and image[nrow][ncol]==inicolor and image[nrow][ncol]!=color:
                    dfs(n,m,nrow,ncol,image,color,delrow,delcol,inicolor)
        inicolor=image[sr][sc]
        n=len(image)
        m=len(image[0])
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        dfs(n,m,sr,sc,image,color,delrow,delcol,inicolor)
        return image
''' Time Complexity--O(n*m)
    Space Complexity--O(n*m)'''
