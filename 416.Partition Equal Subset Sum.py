class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        def subsetsum(ind,nums,target,dp):
            if target==0:
                return True
            if ind==0:
                return target==nums[0]
            if dp[ind][target]!=-1:
                return dp[ind][target]
            nottake=subsetsum(ind-1,nums,target,dp)
            take=False
            if nums[ind]<=target:
                take=subsetsum(ind-1,nums,target-nums[ind],dp)
            dp[ind][target]=take or nottake
            return dp[ind][target]
        target=sum(nums)//2
        dp=[[-1 for j in range(target+1)]for i in range(len(nums))]
        return subsetsum(len(nums)-1,nums,target,dp)
        
