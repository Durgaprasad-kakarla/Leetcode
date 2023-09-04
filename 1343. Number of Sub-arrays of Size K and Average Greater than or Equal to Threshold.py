class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        total=0
        cnt=0
        for i in range(k):
            total+=nums[i]
        if total//k>=threshold:
            cnt+=1
        n=len(nums)
        for i in range(k,n):
            total+=(nums[i]-nums[i-k])
            if total//k>=threshold:
                cnt+=1
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
