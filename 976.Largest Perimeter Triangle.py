class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #Firstly we will sort the nums and reverse it in descending order.
        nums=sorted(nums)[::-1]
        #Now check the condition so that length of one side should be less than length of other two sides 
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
