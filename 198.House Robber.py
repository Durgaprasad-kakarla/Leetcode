class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0
        for n in nums:
            temp=max(n+rob1,rob2)#storing the max value of n+rob1 and rob2
            rob1=rob2
            rob2=temp
        return rob2#return the maximum amount of money
