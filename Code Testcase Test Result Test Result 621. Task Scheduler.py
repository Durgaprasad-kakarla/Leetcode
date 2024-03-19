class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alpha=[0]*26
        for i in range(len(tasks)):
            alpha[ord(tasks[i])-65]+=1
        heap=[]
        for i in range(26):
            if alpha[i]>0:
                heapq.heappush(heap,[-alpha[i],i])
        tot=0
        while heap:
            k=n+1
            vis=[0]*26
            while heap and k>0:
                freq,ele=heapq.heappop(heap)
                alpha[ele]-=1
                vis[ele]=1
                k-=1
                tot+=1
            for i in range(26):
                if vis[i]==1 and alpha[i]>0:
                    heapq.heappush(heap,[-alpha[i],i])
            if heap:
                if k>0:
                    tot+=(k)
        return tot
''' Time Complexity--O(n*k)
    Space Complexity--O(n)'''
