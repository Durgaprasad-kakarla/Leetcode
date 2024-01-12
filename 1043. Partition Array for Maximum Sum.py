class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for ind in range(n-1,-1,-1):
            maxele,maxi=0,-float('inf')
            for i in range(ind,ind+k):
                if i<n:
                    maxele=max(maxele,arr[i])
                    cost=maxele*(i-ind+1)+dp[i+1]
                    maxi=max(maxi,cost)
            dp[ind]=maxi
        return dp[0]
''' Time Complexity--O(n*k)
    Space Complexity--O(n)'''
