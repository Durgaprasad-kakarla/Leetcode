class Solution:
    def digitSum(self, s: str, k: int) -> str:
        #Here we will find sum of the digits of  a number
        def digitsum(n):
            sum1=0
            while n != 0:
                rem = n % 10
                sum1 = sum1 + rem
                n = n // 10
            return sum1

        #here will add string and store in a string 
        def add(s, k):
            s1 = ""
            for i in range(0, len(s), k):
                n = int(s[i:k + i])
                sum1 = digitsum(n)
                s1 = s1 + str(sum1)
            return str(s1)
        #Iterate the loop until we get len(s)<=k
        for i in range(len(s)):
            if len(s) <= k:
                return s
            s = add(s, k)
        
