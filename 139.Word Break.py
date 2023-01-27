class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        if s in wordset:
            return True
        dp={}
        def dfs(s):
            if s in dp:
                return dp[s]
            for i in range(1,len(s)):
                prefix=s[:i]
                suffix=s[i:]
                if (prefix in wordset and suffix in wordset) or (prefix in wordset and dfs(suffix)):
                    dp[s]=True
                    return dp[s]
            dp[s]=False
            return dp[s]
        if dfs(s):
            return True
        else:
            return False
        
