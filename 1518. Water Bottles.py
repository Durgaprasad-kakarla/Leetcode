class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles+(numBottles-1)//(numExchange-1)
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
