class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        if nums[-1]<1:
            return -1
        cnt=0
        for i in range(n-1,-1,-1):
            if nums[i]>=cnt:
                cnt+=1
            else:
                if i<n-1 and nums[i+1]>=cnt:
                    return cnt
                return -1
        print(cnt)
        if nums[0]>=cnt and len(nums)==cnt:
            return cnt
        return -1
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
