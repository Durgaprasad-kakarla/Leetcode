class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxi=0
        for i in range(len(satisfaction)):
            sum1=0
            for j in range(len(satisfaction)):
                sum1+=satisfaction[j]*(j+1)
            maxi=max(sum1,maxi)
            satisfaction.pop(0)
        return maxi
 '''Time Complexity--O(n^2)
    Space Complexity--O(1)'''
