class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-a for a in piles]
        heapq.heapify(piles)#heapifying the piles list
        for i in range(k):
            heapq.heapreplace(piles,piles[0]//2)#replace the piles[0]//2 with piles in the heap
        return -sum(piles)
