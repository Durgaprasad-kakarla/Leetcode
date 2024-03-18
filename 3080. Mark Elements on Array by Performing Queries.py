class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap=[]
        n=len(nums)
        for i in range(n):
            heapq.heappush(heap,[nums[i],i])
        marked=[0]*n
        sm=sum(nums)
        lst=[]
        tot=0
        for ind,k in queries:
            if not marked[ind]:
                marked[ind]=1
                tot+=nums[ind]
            while heap and k>0:
                ele,ind=heapq.heappop(heap)
                if not marked[ind]:
                    tot+=nums[ind]
                    marked[ind]=1
                    k-=1
            lst.append(sm-tot)
        return lst
''' Time Complexity--O(len(queries)*nlogn)
    Space Complexity--O(n)'''
