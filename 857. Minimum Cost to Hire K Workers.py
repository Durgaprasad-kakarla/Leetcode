class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(quality)
        lst=[]
        for i in range(n):
            lst.append([wage[i]/quality[i],quality[i]])
        lst=sorted(lst,key=lambda x:x[0])
        print(lst)
        heap=[]
        tot_money=0
        ans=float('inf')
        for rate,q in lst:
            heapq.heappush(heap,-q)
            tot_money+=q
            if len(heap)>k:
                tot_money+=heapq.heappop(heap)
            if len(heap)==k:
                ans=min(ans,tot_money*rate)
        return ans
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
