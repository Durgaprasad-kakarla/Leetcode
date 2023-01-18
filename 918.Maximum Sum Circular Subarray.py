class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max1,min1=nums[0],nums[0]
        curmax,curmin=0,0
        total=0
        for i in nums:
            curmax=max(curmax+i,i)
            curmin=min(curmin+i,i)
            total+=i
            max1=max(max1,curmax)
            min1=min(min1,curmin)
        return max(max1,total-min1) if max1>0 else max1
            
        
