class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[sys.maxsize for i in range(n)
        ]for j in range(n)]
        for i in edges:
            dist[i[0]][i[1]]=i[2]
            dist[i[1]][i[0]]=i[2]
        for i in range(n):
            dist[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]==sys.maxsize or dist[k][j]==sys.maxsize:
                        continue
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        cntcity=n
        cityno=-1
        for city in range(n):
            cnt=0
            for adjcity  in range(n):
                if dist[city][adjcity]<=distanceThreshold:
                    cnt+=1
            if cnt<=cntcity:
                cntcity=cnt
                cityno=city
        return cityno
''' Time Complexity--O(n^3)
    Space Complexity--O(n^2)'''
