class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=3:
            return 0
        nums.sort()
        return min(nums[n-4]-nums[0],nums[n-1]-nums[3],nums[n-2]-nums[2],nums[n-3]-nums[1])
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
