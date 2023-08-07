class Solution:
    def jump(self, arr: List[int]) -> int:
        def fun(ind,k,arr,dp):
            n=len(arr)
            if ind==n-1:
                return 0
            if ind>n:
                return sys.maxsize
            if dp[ind][k]!=-1:
                return dp[ind][k]
            mini=sys.maxsize
            for i in range(ind+1,ind+k+1):
                if i<n:
                    mini=min(mini,1+fun(i,arr[i],arr,dp))
            dp[ind][k]=mini
            return mini
        n=len(arr)
        dp=[[-1 for i in range(arr[j]+1)]for j in range(n)]
        return fun(0,arr[0],arr,dp)
''' Time Complexity--O(n*n)
    Space Complexity--O(n*n)'''
