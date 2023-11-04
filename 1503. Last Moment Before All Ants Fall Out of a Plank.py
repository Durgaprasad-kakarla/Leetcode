class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        leftmax=sys.maxsize*-1
        rightmin=sys.maxsize
        if left:
            leftmax=max(left)
        if right:
            rightmin=min(right)
        return max(leftmax,n-rightmin)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
