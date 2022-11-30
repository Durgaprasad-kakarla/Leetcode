class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1=Counter(arr)#we will create a dictionary with the count as the value and elements in the array as keys
        if len(set(dict1.values()))==len(dict1.values()):#if the dictionary values are unique it will return True else return False
            return True
        return False
