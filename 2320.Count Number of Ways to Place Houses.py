class Solution:
    def countHousePlacements(self, n: int) -> int:
        a,b,c,i=1,1,0,0
        while i<n:
            c=a+b
            a,b,i=b,c,i+1
        #return Square of the last fibonacci number
        return (c*c)%(10**9+7)
