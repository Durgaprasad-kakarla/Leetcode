class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Reduce the length of the list as it is having the duplicates
        num3=list(set(nums))
        for i,num in enumerate(num3,1):
            if nums.count(num)>len(nums)//2 :
                return num
