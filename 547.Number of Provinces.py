class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis=[0]*len(isConnected)
        n=len(isConnected)
        def dfs(node,adjlist,vis):
            vis[node]=1
            for i in adjlist[node]:
                if not vis[i]:
                    dfs(i,adjlist,vis)
        adjlist=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adjlist[i].append(j)
                    adjlist[j].append(i)
        count=0
        for i in range(n):
            if not vis[i]:
                count+=1
                dfs(i,adjlist,vis)
        return count
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
