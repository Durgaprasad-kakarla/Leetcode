class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count1=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    count1=count1+1
        return count1
