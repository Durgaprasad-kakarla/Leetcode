class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for i in range(len(nums))]
        maxi=1
        for i in range(len(nums)):
            for prev in range(i):
                if nums[prev]<nums[i]:
                    dp[i]=max(dp[i],1+dp[prev])
            maxi=max(maxi,dp[i])
        return maxi
        
