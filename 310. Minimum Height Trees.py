class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=[[] for i in range(n)]
        queue=deque()
        indegree=[0]*n
        vis=[0]*n
        for u,v in edges:
            indegree[u]+=1
            indegree[v]+=1
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            if indegree[i]==1:
                queue.append(i)
        topo=[0]*n
        lst=[]
        while queue:
            cnt=len(queue)
            lst=[]
            for i in range(cnt):
                node=queue.popleft()
                lst.append(node)
                for x in adj[node]:
                    indegree[x]-=1
                    if indegree[x]==1:
                        queue.append(x)
        return lst
''' Time Complexity--O(V+E)
    Space Complexity--O(V)'''
