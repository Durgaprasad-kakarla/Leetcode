class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(board):
            print("dkfn")
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]=='.':
                        for c in range(49,58):
                            if isvalid(board,i,j,chr(c)):
                                board[i][j]=chr(c)
                                if solve(board)==True:
                                    return True
                                else:
                                    board[i][j]='.'
                        return False
            return True
        def isvalid(board,row,col,c):
            for i in range(9):
                if board[i][col]==c:
                    return False
                if board[row][i]==c:
                    return False
                if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)]==c:
                    return False
            return True
        solve(board)
