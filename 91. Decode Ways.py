class Solution:
    def numDecodings(self, s: str) -> int:
        def ispossible(ind,prev):
            return s[prev]!='0' and int(s[prev:ind])<=26
        @lru_cache(None)
        def func(ind,prev):
            n=len(s)
            if ind>n:
                return 0
            if ind==n:
                if ispossible(ind,prev):
                    return 1
                return 0
            l,r=0,0
            if ispossible(ind+2,ind):
                l=func(ind+2,ind)
            if ispossible(ind+1,ind):
                r=func(ind+1,ind)
            return l+r
        return func(0,-1)
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
