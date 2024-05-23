class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def subsets(ind,temp):
            if ind==len(nums):
                if len(temp)>0:
                    return 1
                return 0
            l=0
            if nums[ind]-k not in temp and nums[ind]+k not in temp:
                l=subsets(ind+1,temp+[nums[ind]])
            r=subsets(ind+1,temp)
            return l+r
        return subsets(0,[])
''' Time Complexity--O(2^n*n)
    Space Complexity--O(n)'''
