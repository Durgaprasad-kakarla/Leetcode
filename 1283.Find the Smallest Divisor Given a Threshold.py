class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        while l<=r:
            mid=(l+r)//2
            tot_sum=0
            for i in nums:
                tot_sum+=math.ceil(i/mid)
            if tot_sum>threshold:
                l=mid+1
            else:
                r=mid-1
        return l
''' Time Complexity--O(n*log(max(nums)))
    Space Complexity--O(1)'''
