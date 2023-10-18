class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree=[0]*n
        if not relations:
            return max(time)
        adj=[[] for i in range(n)]
        for i in relations:
            adj[i[0]-1].append(i[1]-1)
        for i in range(n):
            for j in adj[i]:
                indegree[j]+=1
        queue=[]
        max_time=[0]*n
        for i in range(n):
            if indegree[i]==0:
                max_time[i]=time[i]
                queue.append(i)
        while queue:
            node=queue.pop(0)
            for i in adj[node]:
                max_time[i]=max(max_time[i],max_time[node])
                indegree[i]-=1
                if indegree[i]==0:
                    req_time=time[i]+max_time[i]
                    max_time[i]=req_time
                    queue.append(i)
        return max(max_time)
''' Time Complexity--O(V+E)
    Space Complexity--O(V)'''
