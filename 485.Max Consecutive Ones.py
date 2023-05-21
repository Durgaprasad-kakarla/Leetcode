class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                max1=max(max1,count)
                count=0
        return max(max1,count)
''' Time Complexity--O(n)
    Space Complexity--O(1)
