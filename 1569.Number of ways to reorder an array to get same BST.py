class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def func(nums):
            if len(nums)<=2:
                return 1
            left=[num for num in nums if num<nums[0]]
            right=[num for num in nums if num>nums[0]]
            return comb(len(left)+len(right),len(right))*func(left)*func(right)
        return (func(nums)-1)%(10**9+7)
''' Time Complexity--O(2^n)
    Space Complexity--O(n)'''
