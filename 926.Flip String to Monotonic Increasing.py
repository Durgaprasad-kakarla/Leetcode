class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res=0
        count_one=0
        for i in s:
            if i=="1":#if i==1 increment the count
                count_one+=1
            else:#else res will be min of res+1 and count 
                res=min(res+1,count_one)
        return res
