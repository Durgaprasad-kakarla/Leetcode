class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        powers=[1]
        for i in range(1,n):
            powers.append((powers[-1]*2)%(10**9+7))
        ans=0
        for i in range(n):
            ans+=(nums[i]*(powers[i]-powers[n-i-1]))%(10**9+7)
        return ans%(10**9+7)
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
