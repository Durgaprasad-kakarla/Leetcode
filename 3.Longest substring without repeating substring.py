class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        for i in range(1,len(s)+1):
            j=0
            while j<i and max1<len(set(s[j:i])):
                if len(s[j:i])==len(set(s[j:i])) and len(s[j:i])>max1:
                        max1=len(s[j:i])
                j=j+1
        return max1
        
