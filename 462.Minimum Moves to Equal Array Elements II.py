class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n%2==0:
            median=(nums[n//2-1]+nums[n//2])//2
        else:
            median=nums[n//2]
        num_moves=0
        for i in range(n):
            num_moves+=abs(nums[i]-median)
        return num_moves
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
