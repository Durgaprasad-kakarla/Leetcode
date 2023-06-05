class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x=coordinates[1][0]-coordinates[0][0]
        y=coordinates[1][1]-coordinates[0][1]
        if x!=0:
            z=y/x
        for i in range(2,len(coordinates)):
            x1=coordinates[i][0]-coordinates[i-1][0]
            y1=coordinates[i][1]-coordinates[i-1][1]
            if x==0 and x1!=0:
                return False
            elif (x1!=0 and y1/x1!=z) or (x1==0 and x!=0):
                return False
        return True
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
