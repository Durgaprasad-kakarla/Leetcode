class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        i,count=2,1
        while i*i<=num:
            if (num%i)==0:
                if i==num//i:
                    count+=i
                else:
                    count+=(i+num//i)
            i+=1
        return count==num
''' Time Complexity--O(sqrt(n))
    Space Complexity--O(1)'''
