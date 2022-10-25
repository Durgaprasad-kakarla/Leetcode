class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s,s1='',''
        for i in word1:
            s=s+i
        for i in word2:
            s1=s1+i
        if s1==s:
            return True
        else:
            return False
            
