class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=[]
        ans=[]
        n=len(nums)
        for i in range(n):
            if queue!=[] and queue[0]==i-k:
                queue.pop(0)
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop(-1)
            queue.append(i)
            if i>=k-1:
                ans.append(nums[queue[0]])
        return ans 
 ''' Time Complexity--O(n)
     Space Complexity--O(k)'''
