class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #if the array is equal to the ascending or descending order to the array return True else False
        if nums==sorted(nums) or nums==sorted(nums)[::-1]:
            return True
        else:
            return False
          ##(or)
 class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #if last element is less than the first element then reverse the list
        if nums[-1]<nums[0]:
            nums=nums[::-1]
        for i in range(len(nums)-1):
            # As it is in ascending order if any one is greater than the next element then return False 
            if nums[i]>nums[i+1]:
                return False
        return True
