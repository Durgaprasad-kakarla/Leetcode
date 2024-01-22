class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res=[0]*n
        adj=defaultdict(list)
        for i in range(1,n):
            adj[i].append(i+1)
            adj[i+1].append(i)
        adj[x].append(y)
        adj[y].append(x)
        def bfs(i):
            queue=deque()
            vis=set()
            queue.append([i,0])
            vis.add(i)
            while queue:
                i,dist=queue.popleft()
                if dist>0:
                    res[dist-1]+=1
                for node in adj[i]:
                    if node not in vis:
                        vis.add(node)
                        queue.append([node,dist+1])
        for i in range(1,n+1):
            bfs(i)
        return res
''' Time Complexity--O(n^2)
    Space Complexity--O(n)'''
