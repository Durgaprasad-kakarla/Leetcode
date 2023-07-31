class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start,i,count,maxi=0,0,0,0
        n=len(nums)
        while i<n:
            if nums[i]==0:
                count+=1
            if count>k:
                maxi=max(maxi,i-start)
                while count>k:
                    if nums[start]==0:
                        count-=1
                    start+=1
            i+=1
        return max(maxi,i-start)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
