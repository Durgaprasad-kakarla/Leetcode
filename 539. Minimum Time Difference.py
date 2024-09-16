class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points=[]
        for hm in timePoints:
            H,M=hm.split(":")
            tot_minutes=int(H)*60+int(M)
            time_points.append(tot_minutes)
        time_points.sort()
        n=len(timePoints)
        for i in range(n):
            time_points.append(1440+time_points[i])
        mini=float('inf')
        for i in range(1,2*n):
            mini=min(mini,time_points[i]-time_points[i-1])
        return mini
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
