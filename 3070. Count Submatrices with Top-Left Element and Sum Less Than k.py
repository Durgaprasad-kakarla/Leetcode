class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        pref=[[0 for i in range(m)] for j in range(n)]
        cnt=0
        for i in range(n):
            for j in range(m):
                pref[i][j]+=grid[i][j]
                if i>0:
                    pref[i][j]+=pref[i-1][j]
                if j>0:
                    pref[i][j]+=pref[i][j-1]
                if i>0 and j>0:
                    pref[i][j]-=pref[i-1][j-1]
                if pref[i][j]<=k:
                    cnt+=1
        return cnt
''' Time Complexity--O(n*m)
    Space Complexity--O(n*m)'''
