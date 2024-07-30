class Solution:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        pref=[0]*n
        suff=[0]*n
        cnt1,cnt2=0,0
        for i in range(n):
            pref[i]=cnt1
            suff[n-i-1]=cnt2
            if s[i]=='b':
                cnt1+=1
            if s[n-i-1]=='a':
                cnt2+=1
        mini=float('inf')
        for i in range(n):
            mini=min(mini,pref[i]+suff[i])
        return mini
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
