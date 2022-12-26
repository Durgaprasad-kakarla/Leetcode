class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count1=0
        for i,n in enumerate(nums):
            if i>count1:#if i is greater than count1 value then we cannot reach last index of the list
                return False
            count1=max(count1,i+n)#Store maximum value of count1 and i+n
        return True
