class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #add the elemeents of string from s[1] and before s[-1].check if s is present in it or not
        add=s[1:]+s[:-1]
        return s in add
