class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subs(nums):
            if nums == []:
                return [[]]
            x = subs(nums[1:])
            return x + [[nums[0]] + y for y in x]
        nums=subs(nums)
        return list(set(tuple(sorted(sub)) for sub in  nums))#It is used to remove the duplicate subsets from the list of subsets.
