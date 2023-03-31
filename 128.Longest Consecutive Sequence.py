class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        longest=0
        for num in nums:
            if num-1 not in set1:
                curnum=num
                curstreak=1
                while curnum+1 in set1:
                    curnum+=1
                    curstreak+=1
                longest=max(longest,curstreak)
        return longest
        
        
