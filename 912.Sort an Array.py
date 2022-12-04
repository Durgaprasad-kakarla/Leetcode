class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(list1):
            if len(list1)>1:
                mid=len(list1)//2
                leftlist=list1[:mid]
                rightlist=list1[mid:]
                mergesort(leftlist)
                mergesort(rightlist)
                #upto this we divide the array into subarrays
                i,j,k=0,0,0
                #Now we will merge the elements in the left and right lists by comparing the elements in it
                while i<len(leftlist) and j<len(rightlist):
                    if leftlist[i]<rightlist[j]:
                        list1[k]=leftlist[i]
                        i+=1
                        k+=1
                    else:
                        list1[k]=rightlist[j]
                        j+=1
                        k+=1
                #Here we will merge the remaining elements into the list
                while i<len(leftlist):
                    list1[k]=leftlist[i]
                    i+=1
                    k+=1
                while j<len(rightlist):
                    list1[k]=rightlist[j]
                    j+=1
                    k+=1
        mergesort(nums)
        return nums
