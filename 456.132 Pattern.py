class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        curmin=nums[0]
        n=len(nums)
        for i in range(1,n):
            while stack and nums[i]>=stack[-1][0]:
                stack.pop()
            if stack and nums[i]>stack[-1][1]:
                return True
            stack.append([nums[i],curmin])
            curmin=min(curmin,nums[i])
        return False
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
