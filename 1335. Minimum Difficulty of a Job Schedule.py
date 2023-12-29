class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        if len(arr)<d:
            return -1
        @lru_cache(None)
        def func(i,d,cur_max):
            if i==len(arr):
                if d==0:
                    return 0
                else:
                    return float('inf')
            if d==0:
                return float('inf')
            cur_max=max(cur_max,arr[i])
            res=min(func(i+1,d,cur_max),cur_max+func(i+1,d-1,-1))
            return res
        return func(0,d,-1)
''' Time Complexity--O(n^2*d)
    Space Complexity--O(n*d)'''
