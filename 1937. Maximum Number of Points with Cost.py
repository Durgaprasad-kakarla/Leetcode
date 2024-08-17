class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n,m=len(points),len(points[0])
        curr=[-1 for i in range(m)]
        for i in range(m):
            curr[i]=points[0][i]
        for i in range(1,n):
            prev=curr
            pref=[0]*(m)
            suff=[0]*(m)
            pref[0]=prev[0]
            suff[m-1]=prev[m-1]
            for j in range(1,m):
                pref[j]=max(pref[j-1]-1,prev[j])
            for j in range(m-2,-1,-1):
                suff[j]=max(suff[j+1]-1,prev[j])
            curr=[0]*m
            for j in range(m):
                curr[j]=points[i][j]+max(pref[j],suff[j])
        return max(curr)
''' Time Complexity--O(n*m)
    Space Complexity--O(m)'''
