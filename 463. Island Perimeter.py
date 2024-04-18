class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        n,m=len(grid),len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col]==1:
                    dr=[-1,0,1,0]
                    dc=[0,-1,0,1]
                    cnt=0
                    for i in range(4):
                        nrow=row+dr[i]
                        ncol=col+dc[i]
                        if nrow>=0 and ncol>=0 and nrow<n and ncol<m and grid[nrow][ncol]==1:
                            cnt+=1
                    ans+=(4-cnt)
        return ans
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
