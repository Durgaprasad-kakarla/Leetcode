class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total=0
        for i in range(n):
            bi=bin(i)
            if bi.count('1')==k:
                total+=nums[i]
        return total
''' Time Complexity--O(n*len(binary(n)))
    Space Complexity--O(1)'''
