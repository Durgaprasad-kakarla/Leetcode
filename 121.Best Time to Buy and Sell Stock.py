class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]#take minimum price in mini
        profit=0#take profit as zero
        for i in range(1,len(prices)):
            cost=prices[i]-mini#cost is difference between current price and mini
            profit=max(cost,profit)#so the maximum value of cost and profit will be our new profit
            mini=min(mini,prices[i])# we will keep track the minimum value before the index 'i'
        return profit
    
