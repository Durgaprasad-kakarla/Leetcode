class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets==0:
            return 0
        if minutesToTest<minutesToDie:
            return 0
        if buckets==1:
            return 0
        pigs=1
        while math.pow(minutesToTest//minutesToDie+1,pigs)<buckets:
            pigs+=1
        return pigs
''' Time Complexity--O(log(buckets))
    Space Complexity--O(1)'''
