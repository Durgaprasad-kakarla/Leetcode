class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        l=0
        r=len(s)-1
        count=0
        def check(s,l,r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return check(s,l,r-1) or check(s,l+1,r)
        return True
        
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
