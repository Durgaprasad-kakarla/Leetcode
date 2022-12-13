class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums=set(nums)#removing duplicates from the data
        set1=set()
        set1={int((str(i))[::-1]) for i in nums}#reversing numbers in the set'nums'
        return len(set(nums.union(set1)))#finding the length of the nums+set1 elements
