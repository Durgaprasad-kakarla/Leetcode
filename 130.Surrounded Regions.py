class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col,vis,board):
            vis[row][col]=1
            delrow=[-1,0,1,0]
            delcol=[0,1,0,-1]
            m=len(board[0])
            n=len(board)
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and board[nrow][ncol]=="O":
                    dfs(nrow,ncol,vis,board)
        n=len(board)
        m=len(board[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        #Traverse first and last row and then do dfs if we found any "O"
        for j in range(m):
            if not vis[0][j] and board[0][j]=="O":
                dfs(0,j,vis,board)
            if not vis[n-1][j] and board[n-1][j]=="O":
                dfs(n-1,j,vis,board)
        #Traverse first and last column and then do dfs if we found any "O"
        for i in range(n):
            if not vis[i][0] and board[i][0]=="O":
                dfs(i,0,vis,board)
            if not vis[i][m-1] and board[i][m-1]=="O":
                dfs(i,m-1,vis,board)
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j]=="O":
                    board[i][j]="X"
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
