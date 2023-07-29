class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)
        piles.sort()
        start=n-2
        total=0
        for i in range(n//3):
            total+=piles[start]
            start-=2
        return total
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
