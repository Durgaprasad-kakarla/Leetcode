class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=nums[::-1]
        greater_lst=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop(-1)
            if stack:
                greater_lst.insert(0,stack[-1])
            else:
                greater_lst.insert(0,-1)
            stack.append(nums[i])
        return greater_lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
