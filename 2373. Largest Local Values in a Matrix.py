class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(row,col):
            maxi=0
            for i in range(row,row+3):
                for j in range(col,col+3):
                    maxi=max(maxi,grid[i][j])
            return maxi
        n=len(grid)
        m=len(grid[0])
        maxLocal=[[0 for i in range(m-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(m-2):
                maxLocal[i][j]=find_max(i,j)
        return maxLocal
''' Time Complexity--O(n*m*3*3)
    Space Complexity--O(n-2*m-2)'''
