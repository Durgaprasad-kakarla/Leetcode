class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique_list=[]
        total=0
        start=0
        maxi=sys.maxsize*-1
        n=len(nums)
        for i in range(n):
            if nums[i] not in unique_list:
                unique_list.append(nums[i])
                total+=nums[i]
            else:
                maxi=max(maxi,total)
                while nums[start]!=nums[i]:
                    unique_list.pop(0)
                    total-=nums[start]
                    start+=1
                unique_list.pop(0)
                start+=1
                unique_list.append(nums[i])
        return max(maxi,total)
''' Time Complexity--O(n)--approximately
    Space Complexity--O(n)'''
