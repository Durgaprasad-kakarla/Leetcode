class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        adj=[[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and math.sqrt((bombs[i][0]-bombs[j][0])**2+(bombs[i][1]-bombs[j][1])**2)<=bombs[i][2]:
                    adj[i].append(j)
        max1=0
        def dfs(node,count,vis):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,count,vis)
        for i in range(n):
            vis=[0]*n
            count=0
            dfs(i,count,vis)
            x=sum(vis)
            max1=max(max1,x)
        return max1
 ''' Time Complexity--O(n*n)#one 'n' for checking each node and another 'n' for dfs of the each node
     Space Complexity--O(n*n)#for adjacency list'''
