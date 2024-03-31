class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        mini,maxi,badi,=-1,-1,-1
        n=len(nums)
        for i in range(n):
            if nums[i]<minK or nums[i]>maxK:
                badi=i
            if nums[i]==minK:
                mini=i
            if nums[i]==maxK:
                maxi=i
            ans+=max(0,min(maxi,mini)-badi)
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
