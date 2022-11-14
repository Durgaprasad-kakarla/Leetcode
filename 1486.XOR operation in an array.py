class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n==1:
            return start
        a,b=start,start+2
        c=a^b
        i=2
        while i<n:
            b=start+2*i 
            c=c^b 
            i+=1
        return c
