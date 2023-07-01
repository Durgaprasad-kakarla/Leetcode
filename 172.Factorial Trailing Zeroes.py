class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        i=1
        x=1
        while x!=0:
            x=(n//5**i)
            count=count+x
            i+=1
        return count
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
