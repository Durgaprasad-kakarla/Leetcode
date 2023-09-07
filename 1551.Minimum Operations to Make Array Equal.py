class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        for i in range(n):
            arr.append(2*i+1)
        target=sum(arr)//n
        operations=0
        for i in range(n//2):
            operations+=abs(arr[i]-target)
        return operations
''' Time Complexity--O(n)  
    Space Complexity--O(n)'''
