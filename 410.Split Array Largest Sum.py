class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            tot, cnt = 0, 1
            for num in nums:
                if tot+num<=mid: 
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt>k:
                 l= mid+1
            else:  
                r= mid
        return r
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
