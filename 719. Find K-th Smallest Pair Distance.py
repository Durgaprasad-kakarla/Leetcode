class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def func(nums,m):
            n=len(nums)
            l=0
            tot=0
            for i in range(1,n):
                while l<n and nums[i]-nums[l]>m:
                    l+=1 
                tot+=(i-l)
            return tot
        nums.sort()
        l,r=0,max(nums)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if func(nums,mid)>=k:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
''' Time Complexity--O(nlog(max(nums)))
    Space Complexity--O(1)'''
