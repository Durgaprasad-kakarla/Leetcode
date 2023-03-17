class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[1]*n
        count=[1]*n
        maxi=sys.maxsize*-1
        hash=[i for i in range(n)]
        for ind in range(n):
            for prev in range(ind):
                if arr[prev]<arr[ind] and dp[prev]+1>dp[ind]:
                    dp[ind]=dp[prev]+1
                    count[ind]=count[prev]
                elif arr[prev]<arr[ind] and dp[prev]+1==dp[ind]:
                    count[ind]+=count[prev]
            maxi=max(maxi,dp[ind])
        k=0
        for i in range(n):
            if dp[i]==maxi:
                k+=count[i]
        return k
