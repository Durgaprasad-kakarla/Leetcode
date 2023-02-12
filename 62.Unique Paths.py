class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def func(i,j,dp):
            if i==0 and j==0:#It means we reach the goal
                return 1
            if i<0 or j<0:#It means we are out of the given bounded place
                return 0
            if dp[i][j]!=-1:#It means the dp[i][j] is already in dp so we can utilize it
                return dp[i][j]#memoization
            up=func(i-1,j,dp)#moving up direction
            left=func(i,j-1,dp)#moving left direction
            dp[i][j]=up+left
            return dp[i][j]
        dp=[[-1 for j in range(n)]for i in range(m)]
        return func(m-1,n-1,dp)
'''Time Complexity:O(m*n)-->Here as we have used dp matrix for memoization we reduced the time complexity as no of rows*no of columns
    Space Complexity:O((m-1)+(n-1))+O(m*n)-->here m-1+n-1 is for recursion and m*n is for the dp matrix'''
    
