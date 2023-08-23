class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        total,start=10,9
        for i in range(1,n):
            start=start*(10-i)
            total+=start
        return total
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
