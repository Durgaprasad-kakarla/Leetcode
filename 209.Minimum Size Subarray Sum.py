class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        presum=nums[0]
        mini=10000000
        n=len(nums)
        while r<n:
            while presum>target and l<=r:
                mini=min(mini,r-l+1)
                presum-=nums[l]
                l+=1
            if presum>=target:
                mini=min(mini,r-l+1)
            r+=1
            if r<n:
               presum+=nums[r]
        return 0 if mini==10000000 else mini
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
