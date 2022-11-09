class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        count=0
        while count==0:
            if i%n==0 and i%2==0:
                count=1
                return i 
            i+=1
