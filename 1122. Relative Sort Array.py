class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=Counter(arr1)
        new_arr=[]
        for i in arr2:
            new_arr+=[i]*dic[i]
            del dic[i]
        for i in sorted(dic):
            new_arr+=[i]*dic[i]
        return new_arr
''' Time Complexity--O(n1)
    Space Complexity--O(n1)'''
