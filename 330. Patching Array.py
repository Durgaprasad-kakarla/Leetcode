class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i,res,miss=0,0,1
        while miss<=n:
            if i<len(nums) and nums[i]<=miss:
                miss+=nums[i]
                i+=1
            else:
                miss+=miss
                res+=1
        return res
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
