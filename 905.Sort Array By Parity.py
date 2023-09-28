class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]%2!=0 and nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
            if nums[l]%2==0:
                l+=1
            if nums[r]%2!=0:
                r-=1
        return nums
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
