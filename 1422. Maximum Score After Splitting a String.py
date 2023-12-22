class Solution:
    def maxScore(self, s: str) -> int:
        pref,suff=0,0
        n=len(s)
        prefarr,suffarr=[0]*n,[0]*n
        for i in range(n):
            if s[i]=='0':
                pref+=1
            if s[n-i-1]=='1':
                suff+=1
            prefarr[i]=pref
            suffarr[n-i-1]=suff
        maxi=0
        for i in range(n-1):
            maxi=max(maxi,prefarr[i]+suffarr[i+1])
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
