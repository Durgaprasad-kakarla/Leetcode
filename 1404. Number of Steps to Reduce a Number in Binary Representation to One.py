class Solution:
    def numSteps(self, s: str) -> int:
        n=int(s,2)
        cnt=0
        while n!=1:
            if n&1==1:
                n+=1
            else:
                n//=2
            cnt+=1
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
