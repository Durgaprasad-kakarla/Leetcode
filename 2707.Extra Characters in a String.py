class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        def dfs(i,s,dictionary,dp):
            if i==len(s):
                return 0
            if i in dp:
                return dp[i]
            l=1+dfs(i+1,s,dictionary,dp)
            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    r=dfs(j+1,s,dictionary,dp)
                    l=min(l,r)
            dp[i]=l
            return dp[i]
        return dfs(0,s,dictionary,{})
''' Time Complexity--O(n*n*n)
    Space Complexity--O(n)'''
