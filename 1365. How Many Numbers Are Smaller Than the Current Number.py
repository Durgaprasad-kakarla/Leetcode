class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            count1=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    count1=count1+1
            list1.append(count1)
        return list1
