class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        x2,x3,x5=0,0,0
        while n>1:
            ele2,ele3,ele5=2*ugly[x2],3*ugly[x3],5*ugly[x5]
            min_ele=min(ele2,ele3,ele5)
            if min_ele==ele2:
                x2+=1
            if min_ele==ele3:
                x3+=1
            if min_ele==ele5:
                x5+=1
            ugly.append(min_ele)
            n-=1
        return ugly[-1]
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
