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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        ds=disjoint(len(accounts))
        dic={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in dic:
                    dic[mail]=i
                else:
                    ds.unionbyrank(i,dic[mail])
        merged=[[] for i in range(n)]
        for i in dic:
            mail=i
            node=ds.findunionpar(dic[i])
            merged[node].append(mail)
        ans=[]
        for i in range(n):
            if len(merged[i])==0:
                continue
            temp=[accounts[i][0]]+sorted(merged[i])
            ans.append(temp)
        return ans
''' Time Complexity--O(ElogE)  
    Space Complexity--O(n)'''
