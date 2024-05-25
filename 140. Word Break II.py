class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        def wordbreak(ind,temp,ans):
            if ind==n:
                ans.append(" ".join(temp.copy()))
                return 
            for i in range(10):
                if s[ind:ind+i] in wordDict:
                    wordbreak(ind+i,temp+[s[ind:ind+i]],ans)
        ans=[]
        wordbreak(0,[],ans)
        return ans
''' Time Complexity--O(2^n*len(maxword))
    Space Complexity--O(k*l)-->k-Valid sentencers,l-Length of sentences'''
