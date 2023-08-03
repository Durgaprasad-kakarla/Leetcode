class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        dictionary={0:1}
        prefsum,total=0,0
        for i in range(n):
            prefsum+=nums[i]
            remove=prefsum-k
            if remove in dictionary:
                total+=dictionary[remove]
            if prefsum in dictionary:
                dictionary[prefsum]+=1
            else:
                dictionary[prefsum]=1
        return total
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
