class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set1=list(set(nums))
        sum1,sum2=(len(nums)*(len(nums)+1))//2,sum(set1)
        return [sum(nums)-sum(set1),sum1-sum2]
        
