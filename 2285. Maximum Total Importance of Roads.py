class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dic=defaultdict(int)
        for u,v in roads:
            dic[u]+=1
            dic[v]+=1
        values={}
        for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True):
            values[key]=n
            n-=1
        tot=0
        for u,v in roads:
            tot+=(values[u]+values[v])
        return tot
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
