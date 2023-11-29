class Solution:
    def maximumGap(self, arr: List[int]) -> int:
        heap=[]
        for i in arr:
            heapq.heappush(heap,i)
        x=heapq.heappop(heap)
        maxi=0
        while heap:
            y=heapq.heappop(heap)
            maxi=max(maxi,y-x)
            x=y
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
