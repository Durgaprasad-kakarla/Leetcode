class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap=[]
        n=len(nums)
        for i in range(n):
            heapq.heappush(heap,nums[i])
        cnt=0
        while len(heap)>1 and heap[0]<k:
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            heapq.heappush(heap,min(x,y)*2+max(x,y))
            cnt+=1
        return cnt
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
