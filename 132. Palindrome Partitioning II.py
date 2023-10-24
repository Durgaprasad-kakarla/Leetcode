class Solution:
    def minCut(self, s: str) -> int:
        def ispalindrome(i,j,s):
            return s[i:j+1]==s[i:j+1][::-1]
        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            mini=sys.maxsize
            for j in range(i,n):
                if ispalindrome(i,j,s):
                    cost=1+dp[j+1]
                    mini=min(mini,cost)
            dp[i]=mini
        return dp[0]-1
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
