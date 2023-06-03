class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjlist=[[] for i in range(n)]
        for i in range(n):
            adjlist[manager[i]].append(i)
        queue=[]
        queue.append([headID,informTime[headID]])
        vis=[0 for i in range(n)]
        max1=0
        vis[headID]=1
        while queue:
            x,t=queue.pop(0)
            max1=max(max1,t)
            for i in adjlist[x]:
                if not vis[i]:
                    vis[i]=1
                    queue.append([i,t+informTime[i]])
        return max1
''' Time Complexity--O(n+2E)
    Space Complexity--O(n)'''
