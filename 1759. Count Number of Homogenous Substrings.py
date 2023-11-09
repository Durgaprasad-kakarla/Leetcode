class Solution:
    def countHomogenous(self, s: str) -> int:
        cnt=1
        n=len(s)
        tot=0
        if len(s)==1:
            return 1
        for i in range(1,n):
            if s[i-1]==s[i]:
                cnt+=1
            else:
                tot+=(cnt*(cnt+1))//2
                cnt=1
            if i==n-1:
                tot+=(cnt*(cnt+1))//2
        return tot%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
