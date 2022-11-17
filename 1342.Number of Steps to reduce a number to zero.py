class Solution:
    def numberOfSteps(self, num: int) -> int:
        count1=0
        while num!=0:
            if num%2==0:
                num=num//2
                count1=count1+1
            elif num%2!=0:
                num=num-1
                count1=count1+1
        return count1
