class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        n=len(nums)
        for i in range(n):
            mini,maxi=nums[i],nums[i]
            for j in range(i+1,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                total+=(maxi-mini)
        return total
''' Time Complexity--O(n*n)
    Space Complexity--O(1)'''
