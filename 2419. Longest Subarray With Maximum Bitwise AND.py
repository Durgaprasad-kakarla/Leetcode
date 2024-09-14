class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_element=max(nums)
        n=len(nums)
        length,cnt=0,0
        for i in range(n):
            if nums[i]==max_element:
                cnt+=1
                length=max(length,cnt)
            else:
                cnt=0
        return length
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
