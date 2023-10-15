class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def func(ind,cnt,steps,n):
            if ind==n:
                return 0
            if cnt==steps:
                if ind==0:
                    return 1
                return 0
            l=0
            if ind!=0:
                l=func(ind-1,cnt+1,steps,n)
            r=func(ind+1,cnt+1,steps,n)
            s=func(ind,cnt+1,steps,n)
            return l+r+s
        return func(0,0,steps,arrLen)%(10**9+7)
''' Time Complexity---O(arrLen*steps)
    Space Complexity-(arrLen*steps)'''
