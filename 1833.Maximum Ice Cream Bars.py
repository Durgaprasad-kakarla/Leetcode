class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count1=0
        for i in range(len(costs)):
            if costs[i]<=coins:
                coins=coins-costs[i]
                count1+=1
            else:
                break
        return count1
