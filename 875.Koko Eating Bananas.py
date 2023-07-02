class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def func(piles,mid):
            total=0
            n=len(piles)
            for i in range(n):
                total+=math.ceil(piles[i]/mid)
            return total
        l=1
        r=max(piles)
        while l<=r:
            mid=l+((r-l)//2)
            total=func(piles,mid)
            if  total<=h:
                r=mid-1
            else:
                l=mid+1
        return l
''' Time Complexity--O(n*log(max(piles)))
    Space Complexity--O(1)'''
