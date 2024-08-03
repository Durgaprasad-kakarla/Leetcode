class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return  sorted(arr)==sorted(target)
''' Time Complexity--O(nlogn)    
    Space Complexity--O(1)'''
