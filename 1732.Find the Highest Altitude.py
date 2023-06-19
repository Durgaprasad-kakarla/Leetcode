class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largestalt=0
        prefsum=0
        for i in gain:
            prefsum+=i
            largestalt=max(largestalt,prefsum)
        return largestalt
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
