class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i=0
            while i<len(haystack):
                if haystack[i:len(needle)+i]==needle:
                    return i
                i+=1
        return -1
                    
