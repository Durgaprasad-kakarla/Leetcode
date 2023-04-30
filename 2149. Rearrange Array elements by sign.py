class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        neg,pos=1,0
        for i in range(n):
            if nums[i]<0:
                ans[neg]=nums[i]
                neg+=2
            else:
                ans[pos]=nums[i]
                pos+=2
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
