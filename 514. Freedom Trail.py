class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @lru_cache(None)
        def func(ind,k):
            if k==len(key):
                return 0
            mini=float('inf')
            for i in range(len(ring)):
                if ring[i]==key[k]:
                    min_dist=min(abs(i-ind),len(ring)-abs(i-ind))
                    mini=min(mini,min_dist+1+func(i,k+1))
            return mini
        return func(0,0)
''' Time Complexity--O(n*n*k)
    Space Complexity--O(n*k)'''
