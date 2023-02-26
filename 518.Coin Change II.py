class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev=[0 for i in range(amount+1)]
        cur=prev
        for target in range(amount+1):
            if target%coins[0]==0:
                prev[target]=1
        for ind in range(1,len(coins)):
            for target in range(amount+1):
                nottake=prev[target]
                take=0
                if coins[ind]<=target:
                    take=cur[target-coins[ind]]
                cur[target]=take+nottake
            prev=cur
        return prev[target]
