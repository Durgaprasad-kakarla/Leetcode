class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=0,1
        if n==1:
            return 1
        else:
            for i in range(n):
                c=a+b
                a=b
                b=c
        return c
