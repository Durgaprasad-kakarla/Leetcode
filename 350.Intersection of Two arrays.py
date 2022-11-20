class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create two dictionaries with the count of two lists
        dict1=Counter(nums1)
        dict2=Counter(nums2)
        list1=[]
        for i in dict1.keys():
            if i in dict2.keys():
                if dict1[i]<=dict2[i]:
                    #it is used to append the element into the list how much count is present in both the lists
                    for j in range(dict1[i]):
                        list1.append(i)
                else:
                    for j in range(dict2[i]):
                        list1.append(i)
        return list1
