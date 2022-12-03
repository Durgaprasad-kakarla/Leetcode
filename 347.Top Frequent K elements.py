class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1=Counter(nums)
        dict2={}
        #Here we are creating the dictionary with count as key and the list of numbers as the value
        for x,y in dict1.items(): 
            if y in dict2:
                dict2[y].append(x)
            else:
                dict2[y]=[x]
        count1=0
        list1=[]
        #As we have to store the list of elements in decreasing order of their count.so,we have sorted the keys by using reverse=True
        for i in sorted(dict2.keys(),reverse=True):
            if len(list1)<k:
                list1=list1+dict2[i]
                count1+=1
        return list1
