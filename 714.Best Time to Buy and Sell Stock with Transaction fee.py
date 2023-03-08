class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prev=[0 for j in range(2)]
        for ind in range(len(prices)-1,-1,-1):
            cur=[0 for i in range(2)]
            for buy in range(2):
                if buy:
                    print(ind)
                    cur[buy]=max(-prices[ind]+prev[0],prev[1])
                else:
                    cur[buy]=max(prices[ind] + prev[1]-fee,prev[0])
            prev=cur
        return prev[1]
