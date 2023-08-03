class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dictionary={0:1}
        prefsum,total=0,0
        n=len(nums)
        for i in range(n):
            prefsum+=nums[i]
            remove=prefsum-goal
            if remove in dictionary:
                total+=dictionary[remove]
            if prefsum in dictionary:
                dictionary[prefsum]+=1
            else:
                dictionary[prefsum]=1
        return total
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
