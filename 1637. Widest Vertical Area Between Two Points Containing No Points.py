class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxi=0
        for i in range(1,len(points)):
            maxi=max(maxi,points[i][0]-points[i-1][0])
        return maxi
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
