class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()#last element will give us maximum product
        return (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)
