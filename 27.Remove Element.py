class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for r in nums:
            if r!=val:#if the value is not matched with value in the list then store the value in the nums and then increment 'i'
                nums[i]=r
                i=i+1
        return i
