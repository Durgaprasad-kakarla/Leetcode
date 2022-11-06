class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        if j==0: return 0
        count1=0
        #return i when one element is greater than the next element as it is one of the peak element in the array.
        while i<j:
            if nums[i]>nums[i+1]:
                count1+=1
                return i
            i+=1
        #If count==0 means there is no element which is greater than the next so last element is the peak element
        if count1==0:
            return j
