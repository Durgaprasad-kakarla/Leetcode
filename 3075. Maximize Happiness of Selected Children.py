class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap=[]
        for i in happiness:
            heapq.heappush(heap,-i)
        l=0
        tot=0
        while heap and k>0:
            x=heapq.heappop(heap)
            if abs(x)<l:
                return tot
            tot+=(abs(x)-l)
            l+=1
            k-=1
        return tot
''' Time Complexity-O(nlogk)
    Space Complexity--O(n)'''
