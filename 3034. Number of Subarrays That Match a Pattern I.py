class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m=len(pattern)
        n=len(nums)
        cnt=0
        lst=[]
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                lst.append(-1)
            elif nums[i-1]==nums[i]:
                lst.append(0)
            else:
                lst.append(1)
        for i in range(len(lst)):
            for j in range(i+1,len(lst)+1):
                if lst[i:j]==pattern:
                    cnt+=1
        return cnt
''' Time Complexity--O(n^2)
    Space Complexity--O(n)'''
