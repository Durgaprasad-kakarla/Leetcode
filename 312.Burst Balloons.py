class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0 for j in range(n+2)]for i in range(n+2)]
        nums.append(1)
        nums.insert(0,1)
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=sys.maxsize*-1
                for ind in range(i,j+1):
                    cost=nums[i-1]*nums[ind]*nums[j+1]+dp[i][ind-1]+dp[ind+1][j]
                    maxi=max(maxi,cost)
                dp[i][j]=maxi
        return dp[1][n]
