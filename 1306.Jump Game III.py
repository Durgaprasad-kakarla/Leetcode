class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def fun(ind,arr,dp):
            n=len(arr)
            if ind<0 or ind>n-1:
                return False
            if arr[ind]==0:
                dp[ind]=True
                return True
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind]=False
            if fun(ind+arr[ind],arr,dp) or fun(ind-arr[ind],arr,dp):
                dp[ind]=True
                return True
            return False
        dp=[-1 for i in range(len(arr))]
        return fun(start,arr,dp)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
