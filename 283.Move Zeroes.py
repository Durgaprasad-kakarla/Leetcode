class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count1=0
        #Firstly arranging elements at the front in the sequence
        for x in nums:
            if x!=0:
                nums[i]=x
                i+=1
            else:
                count1=count1+1
        #Inserting zeroes at the end
        j=0
        while j<count1:
            nums[i]=0
            i+=1
            j+=1
