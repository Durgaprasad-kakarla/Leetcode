class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum=sum(nums)
        k=(totalsum-target)//2
        if (totalsum-target)<0 or (totalsum-target)%2!=0:
            return 0
        def func(ind,k,nums,dp):
            if ind==0:
                if k==0 and nums[0]==0:
                    return 2
                elif k==0 or k==nums[0]:
                    return 1
                else:
                    return 0
            if dp[ind][k]!=-1:
                return dp[ind][k]
            nottake=func(ind-1,k,nums,dp)
            take=0
            if nums[ind]<=k:
                take=func(ind-1,k-nums[ind],nums,dp)
            dp[ind][k]=take+nottake
            return dp[ind][k]
        dp=[[-1 for j in range(k+1)]for i in range(len(nums))]
        return func(len(nums)-1,k,nums,dp)
