class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i=0
        nums.sort()
        n=len(nums)
        for j in range(n):
            k+=nums[j]
            if k<nums[j]*(j-i+1):
                k-=nums[i]
                i+=1
        return j-i+1
'''Time Complexity--O(nlogn)
   Space Complexity--O(1)'''
