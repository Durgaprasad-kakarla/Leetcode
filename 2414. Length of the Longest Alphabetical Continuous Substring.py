class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n=len(s)
        ele=s[0]
        count=1
        maxcount=1
        for i in range(1,n):
            if ord(ele)+1==ord(s[i]):
                ele=s[i]
                count+=1
            else:
                ele=s[i]
                maxcount=max(maxcount,count)
                count=1
        if count>maxcount:
            return count
        return maxcount
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
