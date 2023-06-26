class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1=[]
        heap2=[]
        n=len(costs)
        total_cost=0
        start=0
        end=n-1
        while k>0:
            while len(heap1)<candidates and start<=end:
                heapq.heappush(heap1,costs[start])
                start+=1
            while len(heap2)<candidates and start<=end:
                heapq.heappush(heap2,costs[end])
                end-=1
            x1=heap1[0] if heap1 else float('inf')
            x2=heap2[0] if heap2 else float('inf')
            if x1<=x2:
                total_cost+=x1
                heapq.heappop(heap1)
            else:
                total_cost+=x2
                heapq.heappop(heap2)
            k-=1
        return total_cost
''' Time Complexity--O(nlogn)
    Space Complexity--O(candidates)
