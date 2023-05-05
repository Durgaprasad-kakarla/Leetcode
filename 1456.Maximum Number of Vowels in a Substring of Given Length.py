class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currcount=0
        n=len(s)
        for i in range(k):
            if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u':
                currcount+=1
        maxcount=currcount
        for i in range(k,n):
            if s[i-k]=='a' or s[i-k]=='e' or s[i-k]=='o' or s[i-k]=='i' or s[i-k]=='u':
                currcount-=1
            if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u':
                currcount+=1
            maxcount=max(maxcount,currcount)
            if maxcount==k:
                return maxcount
        return maxcount 
 ''' Time Complexity--O(n)
     Space Complexity--O(1)'''
