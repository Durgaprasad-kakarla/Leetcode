class Solution:
    def totalMoney(self, n: int) -> int:
        x=0
        i=1
        cnt=1
        tot=0
        while cnt<=n:
            tot+=i
            if cnt%7==0:
                x+=1
                i=x
            i+=1
            cnt+=1
        return tot
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
