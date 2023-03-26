class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        front=[0]*n
        for j in range(n):
            front[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            cur=[0 for i in range(n)]
            for j in range(i,-1,-1):
                d=triangle[i][j]+front[j]
                dg=triangle[i][j]+front[j+1]
                cur[j]=min(d,dg)
            front=cur
        return front[0]
 '''Time Complexity--O(n*n)
    Space Complexity--O(n)'''
