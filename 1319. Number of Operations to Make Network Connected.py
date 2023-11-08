class disjoint:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
    def findunionpar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findunionpar(self.parent[node])
        return self.parent[node]
    def unionbyrank(self,u,v):
        ulp_v=self.findunionpar(u)
        ulp_u=self.findunionpar(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        ds=disjoint(n)
        extra=0
        for i in edges:
            if ds.findunionpar(i[0])==ds.findunionpar(i[1]):
                extra+=1
            else:
                ds.unionbyrank(i[0],i[1])
        cnt=0
        print(ds.parent)
        for i in range(n):
            if ds.parent[i]==i:
                cnt+=1
        ans=cnt-1
        if extra>=ans:
            return ans
        return -1
''' Time Complexity--O(n+e)
    Space Complexity--O(n)'''
