class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=[]
        for i in range(len(nums1)):
            ind=nums2.index(nums1[i])
            count1=0
            for i in range(ind+1,len(nums2),1):
                if nums2[i]>nums2[ind] and count1==0:
                    nums3.append(nums2[i])
                    count1=count1+1
            if count1==0:
                nums3.append(-1)
        return nums3
