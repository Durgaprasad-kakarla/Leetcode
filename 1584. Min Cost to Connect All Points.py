class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        paths = []
        n = len(points)
        each_path = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    each_path.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]),j,i])
            each_path.sort()
            paths.append(each_path)
            each_path = []
        vis=[0]*n
        pq=[]
        heapq.heappush(pq,[0,0,-1])
        cost=0
        while pq:
            top=heapq.heappop(pq)
            dist=top[0]
            node=top[1]
            parent=top[2]
            if vis[node]==1:
                continue
            vis[node]=1
            cost+=top[0]
            for i in paths[node]:
                if not vis[i[1]]:
                    heapq.heappush(pq,[i[0],i[1],node])
        return cost
''' Time Complexity--o(n*n)+O(V*V)
    Space Complexity--O(V*V)'''
