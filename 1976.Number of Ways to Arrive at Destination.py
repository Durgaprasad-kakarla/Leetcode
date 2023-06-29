class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjlist=[[] for i in range(n)]
        for i in range(len(roads)):
            adjlist[roads[i][0]].append([roads[i][1],roads[i][2]])
            adjlist[roads[i][1]].append([roads[i][0],roads[i][2]])
        pq=[]
        heapq.heappush(pq,[0,0])
        dist=[sys.maxsize for i in range(n)]
        c=0
        ways=[0]*n
        ways[0]=1
        minpath=sys.maxsize
        while pq:
            top=heapq.heappop(pq)
            d=top[0]
            node=top[1]
            for i in adjlist[node]:
                adjNode=i[0]
                edN=i[1]
                if dist[adjNode]>d+i[1]:
                    dist[adjNode]=d+edN
                    heapq.heappush(pq,[d+edN,i[0]])             
                    ways[adjNode]=ways[node]
                elif d+edN==dist[adjNode]:
                    ways[adjNode]+=ways[node]
        return (ways[n-1])%(10**9+7)
''' Time Complexity--O(E*logn)-->Here E islen(roads)
    Space Complexity--O(n)'''
