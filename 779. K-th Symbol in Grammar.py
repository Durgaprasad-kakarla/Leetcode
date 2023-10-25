class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def func(n,k):
            if n==1 or k==1:
                return False
            mid=(math.pow(2,n-1))//2
            if k<=mid:
                return func(n-1,k)
            else:
                return not func(n-1,k-mid)
        return 1 if func(n,k) else 0
