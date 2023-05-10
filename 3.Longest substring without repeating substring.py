class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        count=0
        i=0
        n=len(s)
        dict1={}
        while i<n:
            if s[i] in dict1:
                max1=max(max1,count)
                count=0
                i=dict1[s[i]]
                dict1={}
            else:
                dict1[s[i]]=i
                count+=1
            i+=1
        return max(max1,count)
''' Time complexity--O(n*n)
    Space Complexity--O(n)'''
        
