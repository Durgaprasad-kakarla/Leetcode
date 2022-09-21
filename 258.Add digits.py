class Solution:
    def addDigits(self, num: int) -> int:
        str1=str(num)
        # finding the sum of digits of a number
        def digitsum(s):
            n=int(s)
            sum1=0
            while n != 0:
                rem = n % 10
                sum1 = sum1 + rem
                n = n // 10
            return str(sum1)
         #iterate the loop till we get len(str1)==1
        for i in range(len(str1)+1):
            if len(str1)==1:
                return int(str1)
            str1=digitsum(str1)
