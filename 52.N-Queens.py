#USING BACKTRACKING
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board, row, col, n):
            # checking the upper elements of that column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # checking the upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            #checking the upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n, 1)):
                if board[i][j] == 'Q':
                    return False
            return True


        def NQutil(board, row, n):
            if row >= n:
                printsolution(board, n)
                return
            for i in range(n):
                if isSafe(board, row, i, n):
                    board[row][i] = 'Q'
                    if NQutil(board, row + 1, n):
                        return True
                    board[row][i] = '.'
            return False
        list2=[]
        def printsolution(board, n):
            list1=[]
            for i in board:
                s=''
                for j in i:
                    s=s+j
                list1.append(s)
            list2.append(list1)
        board = [['.'for i in range(n)]for j in range(n)]
        NQutil(board,0,n)
        return list2
