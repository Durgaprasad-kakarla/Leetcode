class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n=len(s)
        dp=[0]*26
        for i in range(n):
            maxi=0
            charindex=ord(s[i])-97
            for j in range(k+1):
                if charindex-j>=0:
                    maxi=max(maxi,dp[charindex-j])
            for j in range(k+1):
                if charindex+j<26:
                    maxi=max(maxi,dp[charindex+j])
            dp[charindex]=maxi+1
        return max(dp)
''' Time Complexity--O(n) 
    Space Complexity--O(1)'''
