class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1:
            return False
        dx=abs(sx-fx)
        dy=abs(sy-fy)
        if max(dx,dy)<=t:
            return True
        return False
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
