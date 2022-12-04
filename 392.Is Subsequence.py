class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        while i<len(s) and j<len(t):
            #checking the each character in the s is present in t or not if it is found then increment i else increment j
            if s[i]==t[j]:
                i+=1
            j+=1
        #if i=len(s) then s is a subsequence of t
        if i==len(s):
            return True
        else:
            return False
