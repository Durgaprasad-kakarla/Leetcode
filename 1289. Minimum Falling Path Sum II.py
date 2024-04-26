class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        @lru_cache(None)
        def func(i,j):
            if i<0 or j<0 or j>=m:
                return float('inf')
            if i==0:
                return grid[i][j]
            mini=float('inf')
            for x in range(m):
                if x!=j:
                    mini=min(mini,func(i-1,x)+grid[i][j])
            return mini
        mini=float('inf')
        for i in range(m):
            mini=min(mini,func(n-1,i))
        return mini
''' Time Complexity--O(n*m*m)
    Space Complexity--O(n*m)'''
