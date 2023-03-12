class Solution:
    def countBits(self, n: int) -> List[int]:
        def countset(n):
            res=0
            while n>0:
                n=(n&(n-1))
                res+=1
            return res
        list1=[]
        for i in range(n+1):
            list1.append(countset(i))
        return list1

        
