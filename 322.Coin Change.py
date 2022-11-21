class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Dynamic approach is used to solve this problem by using Bottom Approach
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                #If a>c then we have find the min of them and put it in the list dp
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        #if we don't get any combination to get the required amount then return -1 else print the dp[amount]
        return dp[amount] if dp[amount]!=amount+1 else -1
