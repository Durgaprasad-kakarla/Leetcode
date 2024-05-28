class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        sm,start,maxlen=0,0,0
        for i in range(n):
            sm+=abs(ord(s[i])-ord(t[i]))
            while sm>maxCost:
                sm-=abs(ord(s[start])-ord(t[start]))
                start+=1
            maxlen=max(maxlen,i-start+1)
        return maxlen
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
