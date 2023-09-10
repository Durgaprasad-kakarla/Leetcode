class Solution:
    def countOrders(self, n: int) -> int:
        fact=1
        for i in range(1,n*2+1):
            fact=(fact*i)
        return (fact//(2**n))%(10**9+7)
''' Time Complexity--O(n*2)
    Space Complexity--O(1)'''
