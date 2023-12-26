class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def func(n,target,dp):
            if n==0:
                if target==0:
                    return 1
                return 0
            if dp[n][target]!=-1:
                return dp[n][target]
            cnt=0
            for i in range(1,k+1):
                if target>=i:
                    cnt+=func(n-1,target-i,dp)
                else:
                    break
            dp[n][target]=cnt
            return cnt
        dp=[[-1 for i in range(target+1)]for j in range(n+1)]
        return func(n,target,dp)%(10**9+7)
''' Time Complexity--O(n*k*target)
    Space Complexity--O(n*target)'''
