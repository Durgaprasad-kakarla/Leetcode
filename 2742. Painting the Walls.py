class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        def func(ind,remain,cost,time,dp):
            if remain<=0:
                return 0
            if ind==len(cost):
                return sys.maxsize
            if dp[ind][remain]!=-1:
                return dp[ind][remain]
            l=func(ind+1,remain,cost,time,dp)
            r=func(ind+1,remain-1-time[ind],cost,time,dp)+cost[ind]
            dp[ind][remain]=min(l,r)
            return min(l,r)
        dp=[[-1 for i in range(len(cost)+1)]for j in range(len(cost))]
        return func(0,len(cost),cost,time,dp)
''' Time Complexity--O(n*n)
    Space Compelxity--O(n*n)'''
