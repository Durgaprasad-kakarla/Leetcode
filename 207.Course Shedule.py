class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1
        queue=[]
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node=queue.pop()
            topo.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(topo)==numCourses:
            return True
        return False
''' Time Complexity--O(V+E)--->V is vertices and E is edges
    Space Complexity--O(V)
