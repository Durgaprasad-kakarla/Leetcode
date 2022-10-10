class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(itertools.permutations(nums)))#Itertools is good package for permuations
