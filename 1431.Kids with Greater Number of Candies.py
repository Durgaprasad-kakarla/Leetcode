class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1=max(candies)
        list1=[]
        for i in candies:
            if i+extraCandies>=max1:
                list1.append(True)
            else:
                list1.append(False)
        return list1
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
