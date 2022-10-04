class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if max(nums)*(max(nums)+1)//2==sum(nums):
            if 0 not in nums:
                return 0
            return max(nums)+1
        return max(nums)*(max(nums)+1)//2-sum(nums)
