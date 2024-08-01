class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for st in details:
            if int(st[-4:-2])>60:
                cnt+=1
        return cnt 
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
