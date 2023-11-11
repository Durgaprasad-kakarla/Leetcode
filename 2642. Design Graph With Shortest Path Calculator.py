class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj=[[] for i in range(n)]
        self.val=n
        for i in edges:
            x=[i[1],i[2]]
            self.adj[i[0]].append(x)
    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append([edge[1],edge[2]])

    def shortestPath(self, node1: int, node2: int) -> int:
        priority_queue = [(0, node1)]
        dist = [float('inf')] * self.val
        dist[node1] = 0
        while priority_queue:
            dis, node = heapq.heappop(priority_queue)
            for adjNode, edgW in self.adj[node]:
                if dis + edgW < dist[adjNode]:
                    dist[adjNode] = dis + edgW
                    heapq.heappush(priority_queue, (dist[adjNode], adjNode))
        if dist[node2]==float('inf'):
            return -1
        return dist[node2]
            
        

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
''' Time Complexity--O(Elogn)
    Space Complexity--O(n)'''
