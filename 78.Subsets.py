class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(nums):
            if nums == []:
                return [[]]
            x = subs(nums[1:])
            return x + [[nums[0]] + y for y in x]
        return subs(nums)
