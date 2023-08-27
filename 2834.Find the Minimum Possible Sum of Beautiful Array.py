class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        total,i=1,2
        dictionary={1:1}
        while n-1>0:
            if target-i not in dictionary:
                total+=i
                dictionary[i]=1
                n-=1
            i+=1
        return total
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
