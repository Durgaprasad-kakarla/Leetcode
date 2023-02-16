class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def uniquepaths(i,j,dp,obstacleGrid):
            if i==0 and j==0:
                return 2
            if i<0 or j<0:
                return 0
            if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=uniquepaths(i-1,j,dp,obstacleGrid)
            left=uniquepaths(i,j-1,dp,obstacleGrid)
            dp[i][j]=up+left
            return dp[i][j]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        dp=[[-1 for j in range(n)]for i in range(m)]
        
        return (uniquepaths(m-1,n-1,dp,obstacleGrid)//2)%(2*(10)**9)
'''Time Complexity:O(m*n)-----Space Complexity:O(m*n+(m-1)+(n-1))
