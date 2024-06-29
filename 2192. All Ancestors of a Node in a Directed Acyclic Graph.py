class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
        mat=[]
        for i in range(n):
            vis=[0 for i in range(n)]
            dfs(i)
            for j in range(n):
                if vis[i]==1 and j!=i:
                    lst.append(j)
            mat.append(lst)
        final=[]
        for i in range(n):
            lst=[]
            for j in range(n):
                if mat[j][i]==1 and j!=i:
                    lst.append(j)
            final.append(lst)
        return final
''' Time Complexity--O(n*n)
    Space Complexity--O(n*n)'''
