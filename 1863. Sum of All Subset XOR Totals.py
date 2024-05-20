class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def subsequence(ind,sm):
            if ind<0:
                return sm
            return subsequence(ind-1,sm^nums[ind])+subsequence(ind-1,sm)
        return subsequence(n-1,0)
''' Time Complexity--O(2^n)
    Space Complexity--O(1)'''
