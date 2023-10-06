class Solution:
    def integerBreak(self, n: int) -> int:
        x=n//2
        maxi=0
        if n==3:
            return 2
        while x!=0:
            l=n//x
            if n%x!=0:
                total=(x**(l-1))*(x+n%x)
                maxi=max(x**(l)*(n%x),maxi)
            else:
                total=(x**l)
            maxi=max(maxi,total)
            x-=1
        return maxi
''' Time Complexity--O(n//2)
    Space Complexity--O(1)'''
