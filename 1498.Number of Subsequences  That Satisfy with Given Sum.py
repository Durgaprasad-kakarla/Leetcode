class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        r=len(nums)-1
        for i,left in enumerate(nums):
            while left+nums[r]>target and i<=r:
                r-=1
            if i<=r:
                count+=2**(r-i)
        return count%(10**9+7)
''' Time Complexity--O(n^2+nlogn)
    Space Complexity--O(1)
