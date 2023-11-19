class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        tot=0
        n=len(nums)
        nums.sort()
        for i in range(n-2,-1,-1):
            if nums[i]!=nums[i+1]:
                tot=tot+(n-i-1)
        return tot
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
