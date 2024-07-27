class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_lst=[[] for i in range(26)]
        n=len(original)
        for i in range(n):
            adj_lst[ord(original[i])-97].append([ord(changed[i])-97,cost[i]])
        length=len(source)
        def func(src):
            heap=[]
            dist=[float('inf')]*26
            dist[src]=0
            heapq.heappush(heap,[0,src])
            while heap:
                cost,node=heapq.heappop(heap)
                for i,c in adj_lst[node]:
                    if dist[i]>cost+c:
                        dist[i]=cost+c
                        heapq.heappush(heap,[cost+c,i])
            return dist
        tot_cost=0
        dist=[[float('inf') for j in range(26)] for i in range(26)]
        st=set(original)
        for i in range(26):
            dist[i]=func(i)
        for i in range(length):
            if dist[ord(source[i])-97][ord(target[i])-97]==float('inf'):
                return -1
            tot_cost+=dist[ord(source[i])-97][ord(target[i])-97]
        return tot_cost
'''Time Complexity--O(length)
   Space Complexity--O(1)'''
