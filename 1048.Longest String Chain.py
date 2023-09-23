class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dictionary={}
        for i in words:
            dictionary[i]=len(i)
        dic=sorted(dictionary.items(),key=lambda x:x[1])
        words=[]
        for i in dic:
            words.append(i[0])
        n=len(words)
        print(words)
        dp=[1]*n
        def issubsequence(s,t):
            i,j=0,0
            if len(s)!=len(t)+1:
                return False
            while i<len(s):
                if  j<len(t) and s[i]==t[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if i==len(s) and j==len(t):
                return True
            else:
                return False
        maxi=1
        for i in range(n):
            for prev in range(i):
                x=issubsequence(words[i],words[prev])
                if issubsequence(words[i],words[prev]) and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
            maxi=max(maxi,dp[i])
        return maxi
''' Time Complexity--O(n*n*l)--l-->len(word)
    Space Complexity--(n)'''
