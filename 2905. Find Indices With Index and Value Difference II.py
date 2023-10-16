class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        maxi,mini=0,0
        n=len(nums)
        for i in range(indexDifference,n):
            if nums[i-indexDifference]>nums[maxi]:
                maxi=(i-indexDifference)
            if nums[i-indexDifference]<nums[mini]:
                mini=(i-indexDifference)
            if abs(nums[i]-nums[maxi])>=valueDifference:
                return [maxi,i]
            if abs(nums[i]-nums[mini])>=valueDifference:
                return [mini,i]
        return [-1,-1]
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
