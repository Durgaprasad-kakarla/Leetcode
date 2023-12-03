class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        cnt=0
        for i in range(1,n):
            x=points[i-1]
            y=points[i]
            maxi=max(abs(y[0]-x[0]),abs(y[1]-x[1]))
            cnt+=maxi
        return cnt

''' Time Complexity--O(n)  
    Space Complexity--O(1)'''
