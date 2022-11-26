'''Intuition:
we know that the elements are unique so we can solve this using sets

Approach:
setA={1,2,3,4,5,6},setB={4,5,6} then setA-setB={1,2,3},so we have to create set with length of the given list from 1 to len(nums) and set of given list and the difference of those two sets is our required output.

Complexity:
Time complexity:O(n)
Space complexity:O(1)'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list({i for i in range(1,len(nums)+1)}-set(nums))
