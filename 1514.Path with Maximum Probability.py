class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjlist=[[] for i in range(n)]
        for i in range(len(edges)):
            adjlist[edges[i][0]].append([edges[i][1],-(math.log(succProb[i]))])
            adjlist[edges[i][1]].append([edges[i][0],-(math.log(succProb[i]))])
        pq=[]
        heapq.heappush(pq,[0,start])
        dist=[sys.maxsize for i in range(n)]
        maxprob=0
        while pq:
            top=heapq.heappop(pq)
            dis=top[0]
            node=top[1]
            if node==end:
                maxprob=max(maxprob,math.exp(-dis))
            else:
                for i in adjlist[node]:
                    if dist[i[0]]>dis+i[1]:
                        dist[i[0]]=dis+i[1]
                        heapq.heappush(pq,[dist[i[0]],i[0]])
        return maxprob
''' Time Complexity--O(E*logn)
    Space Complexity--O(n)'''
