class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj=[[] for i in range(n)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        heap=[]
        if disappear[0]<1:
            return [-1]*n
        heapq.heappush(heap,[0,0])
        dist=[float('inf') for i in range(n)]
        while heap:
            d,node=heapq.heappop(heap)
            if dist[node]==float('inf') and disappear[node]<=d:
                continue
            if dist[node]!=float('inf'):
                continue
            dist[node]=d
            for i,wt in adj[node]:
                if dist[i]==float('inf'):
                    heapq.heappush(heap,[d+wt,i])
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
''' Time Complexity--O(V+E)
    Space Complexity--O(V)'''
