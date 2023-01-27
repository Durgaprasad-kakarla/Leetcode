class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset=set(words)
        dp={}
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1,len(word)):
                prefix=word[:i]
                suffix=word[i:]
                if((prefix in wordset and suffix in wordset) or (prefix in wordset and dfs(suffix))):
                    dp[word]=True
                    return dp[word]
            dp[word]=False
            return dp[word]
        res=[]
        for w in words:
            if dfs(w):
               res.append(w)
        return res       
