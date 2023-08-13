class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        changed=False
        for i in range(n-1):
            if nums[i]<=nums[i+1]:
                continue
            if changed:
                return False
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            changed=True
        return True
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
