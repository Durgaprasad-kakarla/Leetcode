class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def func(i,j,x,board,vis,word):
            m=len(board)
            n=len(board[0])
            if i<0 or j<0 or i>=m or j>=n:
                return False
            if not vis[i][j] and board[i][j]==word[x] and x==len(word)-1:
                return True
            if board[i][j]==word[x] and not vis[i][j]:
                vis[i][j]=1
                if func(i+1,j,x+1,board,vis,word) or func(i,j+1,x+1,board,vis,word) or func(i-1,j,x+1,board,vis,word) or func(i,j-1,x+1,board,vis,word):
                    return True
                else:
                    vis[i][j]=0
            return False
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    vis=[[0 for i in range(n)] for j in range(m)]
                    if func(i,j,0,board,vis,word):
                        return True
        return False
''' Time Complexity--O(m*n*4^L)
    Space Complexity--O(m*n)'''
