class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def func(n):
            sm=0
            while n!=0:
                sm+=n%10
                n//=10 
            return sm
        st=''
        n=len(s)
        for i in range(n):
            st+=str(ord(s[i])-96)
        num=int(st)
        while k>0 and num>9:
            num=func(num)
            k-=1
        return num
''' Time Complexity--O(n*k)
    Space Complexity--O(1)'''
