class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dictionary=dict(Counter(nums))
        mat=[]
        while sum(dictionary.values()):
            new_list=[]
            for i in dictionary:
                if dictionary[i]>0:
                    new_list.append(i)
                    dictionary[i]-=1
            mat.append(new_list)
        return mat
''' Time Complexity--O(most_frequent_element*distinct_elements)
    Space Complexity--O(distinct_elements)'''
