class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def add(nums):
            num1 = []
            for i in range(len(nums) - 1):
                num1.append((nums[i] + nums[i + 1]) % 10)
            return num1


        for i in range(len(nums)):
            if len(nums) == 1:
                return sum(nums)
            nums = add(nums)
