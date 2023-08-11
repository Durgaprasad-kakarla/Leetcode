class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        n=len(nums)
        dp={}
        ans=1
        for i in range(n):
            num=nums[i]
            if num-difference in dp:
                dp[num]=dp[num-difference]+1
            else:
                dp[num]=1
            ans=max(ans,dp[num])
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
