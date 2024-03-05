class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        l,r=0,n-1
        while l<r and s[l]==s[r]:
            ele=s[l]
            l=l+1
            while l<r and s[l]==ele:
                l+=1
            r-=1
            while l<r and s[r]==ele:
                r-=1
                f1=1
        return r-l+1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
