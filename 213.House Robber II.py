class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbery(nums):
            rob1,rob2=0,0
            for n in nums:
                temp=max(rob1+n,rob2)#maximum element of the rob1+n and rob2
                rob1=rob2
                rob2=temp
            return rob2
        return max(nums[0],robbery(nums[1:]),robbery(nums[:-1]))#maximum element of the  first element and robbery(list from second element and list before last element)
