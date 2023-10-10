class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length=len(nums)
        nums=sorted(set(nums))
        res=length
        r=0
        for l in range(len(nums)):
            while r<len(nums) and nums[r]<length+nums[l]:
                r+=1
            window=r-l
            res=min(res,length-window)
        return res
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
