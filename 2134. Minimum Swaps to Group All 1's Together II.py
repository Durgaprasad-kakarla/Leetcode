class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        tot=nums.count(1)
        nums=nums+nums
        cnt=0
        for i in range(tot):
            if nums[i]==1:
                cnt+=1
        maxi=cnt
        for i in range(tot,len(nums)):
            cnt+=(nums[i]-nums[i-tot])
            maxi=max(maxi,cnt)
        return tot-maxi
''' Time Complexity--O(2*n)
    Space Complexity--O(n)'''
