class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Reduce the list elements to get less time complexity
        num3=list(set(nums))
        list1=[]#this list is used to store the element
        for i,num in enumerate(num3,1):
            #store the elements in the list1 which are having count more than length/3
            if nums.count(num)>len(nums)//3:
                list1.append(num)
        return list1
