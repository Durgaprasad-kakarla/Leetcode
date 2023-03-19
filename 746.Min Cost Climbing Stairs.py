class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            l=cost[i]+dp[i-1]
            r=cost[i]+dp[i-2]
            dp[i]=min(l,r)
        return min(dp[n-1],dp[n-2])
       
