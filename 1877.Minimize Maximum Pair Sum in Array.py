class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        maxsum=0
        for i in range(n//2):
            sum=nums[i]+nums[n-i-1]
            maxsum=max(maxsum,sum)
        return maxsum
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
