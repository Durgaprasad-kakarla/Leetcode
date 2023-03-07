class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=[0 for j in range(2)]
        for ind in range(len(prices)-1,-1,-1):
            cur=[0 for j in range(2)]
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+prev[0],prev[1])
                else:
                    profit=max(prices[ind]+prev[1],prev[0])
                cur[buy]=profit
            prev=cur
        return prev[1]
