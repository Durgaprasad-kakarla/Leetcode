class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        #store the anagrams in the sorted str index
        for i in strs:
            if str(sorted(i)) not in dict1.keys():
                dict1[str(sorted(i))]=list([i])
            else:
                dict1[str(sorted(i))].append(i)
        list1=[]
        #Put all the groups of anagrams in the list
        for i in dict1.keys():
            list1.append(dict1[i])
        return list1
