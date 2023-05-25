class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1#to maintain the count of two
        l=0
        for i in range(1,len(nums)):
            #if the count is not 2 then store second element
            if nums[i]==nums[l] and count<2:
                l+=1
                nums[l]=nums[i]
                count+=1
            # if the elements are same but count is greater than 1 then increment count
            elif nums[i]==nums[l] and count>1:
                count+=1
            #if the elements are not same store that element in the place of l.
            else:
                l+=1
                nums[l]=nums[i]
                count=1
        return l+1
 ''' Time Complexity--O(n)
     Space Complexity--O(1)
