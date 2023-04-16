class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r=r-1
            else:
                l=l+1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
