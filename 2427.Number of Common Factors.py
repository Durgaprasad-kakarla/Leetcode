class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count1=0
        m=min(a,b)#take the minimum element and find all factor common to both a and b and count them finally return count of common elements
        for i in range(1,m+1):
            if a%i==0 and b%i==0:
                count1=count1+1
        return count1
