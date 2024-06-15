class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        maxprofits=[]
        mincapital=[]
        for i in range(n):
            heapq.heappush(mincapital,(capital[i],profits[i]))
        for i in range(k):
            while mincapital and mincapital[0][0]<=w:
                c,p=heapq.heappop(mincapital)
                heapq.heappush(maxprofits,-p)
            if not maxprofits:
                break
            w+=-heapq.heappop(maxprofits)
        return w
''' Time Complexity--O(k*logn)
    Space Complexity--O(n)'''
