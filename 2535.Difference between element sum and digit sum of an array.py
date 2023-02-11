class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele=sum(nums)
        dig=0
        for n in nums:
            if len(str(n))==1:
                dig+=n
            else:
                for i in str(n):
                    dig+=int(i)
        return abs(dig-ele)
