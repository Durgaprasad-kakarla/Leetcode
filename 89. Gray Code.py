class Solution:
    def grayCode(self, n: int) -> List[int]:
        def int_to_binary(n,x):
            s=''
            if n==0:
                return '0'*x
            while n>1:
                rem=n%2
                s=str(rem)+s
                n=n//2
            if len(s)<x:
                s='0'*(x-len(s)-1)+'1'+s
            return s
        def binary_to_gray(s):
            st=s[0]
            n=len(s)
            for i in range(1,n):
                st+=str(int(s[i-1])^int(s[i]))
            return st
        lst=[]
        for i in range(2**n):
            s=int_to_binary(i,n)
            s=int(binary_to_gray(s),2)
            lst.append(s)
        return lst
''' Time Complexity--O(2^n) 
    Space Complexity--O(bin(n))
