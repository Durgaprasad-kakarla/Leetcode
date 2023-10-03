class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        stack=[0]
        nums=[0]+nums
        n=len(nums)
        result=[0]*n
        for i in range(n):
            while nums[stack[-1]]>nums[i]:
                stack.pop()
            j=stack[-1]
            result[i]=result[j]+(i-j)*nums[i]
            stack.append(i)
        return sum(result)%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
