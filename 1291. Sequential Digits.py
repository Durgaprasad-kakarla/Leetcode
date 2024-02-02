class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lst=[12,23,34,45,56,67,78,89,123,234,345,456,567,678,
        789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,
        56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        if low==high:
            return []
        l=0
        r=len(lst)-1
        while l<len(lst) and low>lst[l]:
            l+=1
        while r>0 and high<lst[r]:
            r-=1
        return lst[l:r+1]
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
