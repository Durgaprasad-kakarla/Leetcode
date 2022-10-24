import collections
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        dict1 = collections.defaultdict(list)
        #take the dictionary which can have list as a value
        for i in range(len(nums)):
             dict1[nums[i]].append(i+1)
        for i in dict1.keys():
            #check that the number has duplicates and then find the absolute difference of indices of duplicate numbers
            if len(dict1.get(i))>1:
                list2=dict1.get(i)
                for j in range(1,len(list2)):
                    if list2[j]-list2[j-1]<=k:
                        return True
        return False
