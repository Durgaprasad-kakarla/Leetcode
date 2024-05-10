class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        heap=[]
        for i in range(n):
            for j in range(i+1,n):
                heapq.heappush(heap,[arr[i]/arr[j],arr[i],arr[j]])
        while heap and k>0:
            _,i,j=heapq.heappop(heap)
            k-=1
        return [i,j]
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
