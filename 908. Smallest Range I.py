class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if (max(nums)-k)-(k+min(nums))>0:
            return (max(nums)-k)-(k+min(nums))
        return 0
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
