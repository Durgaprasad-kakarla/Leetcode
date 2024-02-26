class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n=len(bottomLeft)
        def findarea(bottomLeft1,topRight1,bottomLeft2,topRight2):
            xbottomLeft=max(bottomLeft1[0],bottomLeft2[0])
            ybottomLeft=max(bottomLeft1[1],bottomLeft2[1])
            xtopRight=min(topRight1[0],topRight2[0])
            ytopRight=min(topRight1[1],topRight2[1])
            if xtopRight>xbottomLeft and ytopRight>ybottomLeft:
                side=min(xtopRight-xbottomLeft,ytopRight-ybottomLeft)
                return side*side
            return 0
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                maxi=max(maxi,findarea(bottomLeft[i],topRight[i],bottomLeft[j],topRight[j]))
        return maxi
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
