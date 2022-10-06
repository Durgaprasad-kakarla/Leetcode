class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones=list(stones)
        count1=0
        for i in jewels:
            count1=count1+stones.count(i)
        return count1
