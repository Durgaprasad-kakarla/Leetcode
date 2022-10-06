class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count1=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                #finding the pairs which are good that satisfy following conditions.
                if nums[i]==nums[j] and i<j:
                    count1=count1+1#count them to know how many good pairs are present in it.
        return count1
