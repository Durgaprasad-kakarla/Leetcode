class Solution:
    def knightDialer(self, n: int) -> int:
        dic={0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        if n==1:
            return 10
        @lru_cache(None)
        def func(n,x):
            if x==0:
                return 1
            cnt=0
            for i in dic[n]:
                cnt+=func(i,x-1)
            return cnt
        tot=0
        for i in range(10):
            if i!=5:
                tot+=func(i,n-1)
        return (tot)%(10**9+7)
''' Time Complexity--O(9*n)
    Space Complexity--O(9*n)'''
