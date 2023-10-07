class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(i,maxi,remain,n,m):
            if i==n:
                if remain==0:
                    return 1
                return 0
            ans=(maxi*(dp(i+1,maxi,remain,n,m)))
            for x in range(maxi+1,m+1):
                ans=(ans+dp(i+1,x,remain-1,n,m))
            return ans
        return dp(0,0,k,n,m)%(10**9+7)
''' Time Complexity--O(n*m*k)
    Space Complexity--O(n*m*k)'''
