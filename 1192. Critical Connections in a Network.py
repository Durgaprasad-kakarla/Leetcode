class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        global timer
        timer=1
        def dfs(node,parent,vis,adj,tin,low,bridges):
            global timer
            vis[node]=1
            tin[node]=low[node]=timer
            timer+=1
            for i in adj[node]:
                if i==parent:
                    continue
                if vis[i]==0:
                    dfs(i,node,vis,adj,tin,low,bridges)
                    low[node]=min(low[node],low[i])
                    if low[i]>tin[node]:
                        bridges.append([i,node])
                else:
                    low[node]=min(low[node],low[i])
        adj=[[] for i in range(n)]
        print(adj)
        for i in connections:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        vis=[0]*n
        tin=[0]*n
        low=[0]*n
        bridges=[]
        dfs(0,-1,vis,adj,tin,low,bridges)
        return bridges
''' Time Complexity--O(V+2E)
    Space Complexity--O(V+2E)'''
