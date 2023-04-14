class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfscheck(node,graph,vis,pathvis,check):
            vis[node]=1
            pathvis[node]=1
            check[node]=0
            for i in graph[node]:
                if not vis[i]:
                    if dfscheck(i,graph,vis,pathvis,check)==True:
                        check[node]=0
                        return True
                elif pathvis[i]:
                    check[node]=0
                    return True
            check[node]=1
            pathvis[node]=0
            return False
        n=len(graph)
        vis=[0]*n
        pathvis=[0]*n
        check=[0]*n
        for i in range(n):
            if not vis[i]:
                dfscheck(i,graph,vis,pathvis,check)
        safenodes=[]
        for i in range(n):
            if check[i]==1:
                safenodes.append(i)
        return safenodes
''' Time Complexity--O(n+2E)
    Space Compexity--O(n)'''
