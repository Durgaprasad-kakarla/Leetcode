class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        tot=0
        prev=-1
        for s in bank:
            cnt=0
            for i in range(len(s)):
                if int(s[i])&1==1:
                    cnt+=1
            if prev!=-1 and cnt>0:
                tot+=prev*cnt
            if cnt>0:
                prev=cnt
        return tot
''' Time Complexity--O(n*s)
    Space Complexity--O(1)'''
