class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=0,1,1
        flag=0
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n):
                d=a+b+c
                a=b
                b=c
                c=d
            return c
