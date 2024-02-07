class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        count=0
        for i in range(n):
            ax,ay=points[i]
            for j in range(n):
                if i==j:
                    continue
                bx,by=points[j]
                if bx>=ax and by<=ay:
                    found=False
                    for k in range(n):
                        if k!=i and k!=j:
                            cx,cy=points[k]
                            if ax<=cx<=bx and by<=cy<=ay:
                                found=True
                    if not found:
                        count+=1
        return count
''' Time Complexity--O(n^3)
    Space Complexity--O(1)'''
