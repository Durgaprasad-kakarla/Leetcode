class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj=collections.defaultdict(list)
        for i,dst in enumerate(edges):
            adj[i].append(dst)
        def bfs(src,distmap):
            q=deque()
            q.append([src,0])
            distmap[src]=0
            while q:
                node,dst=q.popleft()
                for nei in adj[node]:
                    if nei not in distmap:
                        q.append([nei,dst+1])
                        distmap[nei]=dst+1
        node1dist={}
        node2dist={}
        bfs(node1,node1dist)
        bfs(node2,node2dist)
        res=-1
        resdist=float("inf")
        for i in range(len(edges)):
            if i in node1dist and i in node2dist:
                dist=max(node1dist[i],node2dist[i])
                if dist<resdist:
                    res=i
                    resdist=dist
        return res
