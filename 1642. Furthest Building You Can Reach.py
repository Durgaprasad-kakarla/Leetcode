class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        sm=0
        n=len(heights)
        for i in range(1,n):
            diff=heights[i]-heights[i-1]
            if diff>0:
                if len(heap)<ladders:
                    heapq.heappush(heap,diff)
                else:
                    if heap and diff>heap[0]:
                        heapq.heappush(heap,diff)
                        sm+=heapq.heappop(heap)
                    else:
                        sm+=diff
                    if sm>bricks:
                        return i-1
        return n-1
''' Time Complexity--O(n)
    Space Complexity--O(ladders)'''
