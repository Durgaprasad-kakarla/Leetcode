class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq=[]
        n=len(heights)
        m=len(heights[0])
        dist=[[sys.maxsize for i in range(m)]for j in range(n)]
        dist[0][0]=0
        heapq.heappush(pq,[0,[0,0]])
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        while pq:
            top=heapq.heappop(pq)
            diff=top[0]
            row=top[1][0]
            col=top[1][1]
            if row==n-1 and col==m-1:
                return diff
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    neweffort=max(abs(heights[row][col]-heights[nrow][ncol]),diff)
                    if neweffort<dist[nrow][ncol]:
                        dist[nrow][ncol]=neweffort
                        heapq.heappush(pq,[neweffort,[nrow,ncol]])
        return 0
''' Time Complexity--O(n*m*log(n*m))
    Space complexity--O(n*m)'''
