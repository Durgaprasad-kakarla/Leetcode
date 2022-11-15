class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        count1=0
        for i in dict1.keys():
            if dict1[i]==1:
                count1=count1+i
        return count1
