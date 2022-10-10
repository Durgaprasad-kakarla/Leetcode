class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=None
        k=len(nums)
        #Firstly find the pivot and the index of the pivot,here pivot is number to be swapped
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pivot=nums[i-1]
                print(i-1)
                d=i-1
                break
        #If there is no pivot then reverse the list to get next permutation
        if pivot is None:
            nums.reverse()
        else:
            #find the element to be swapped with the pivot
            while(d<k):
                if pivot < nums[k-1]:
                    print("lsdnf")
                    l=k-1
                    break
                k=k-1
            nums[d],nums[l]=nums[l],nums[d]
            #After swapping reverse the elements after the pivot element
            nums[d+1:]=nums[d+1:][::-1]
            
