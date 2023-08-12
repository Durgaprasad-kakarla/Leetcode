class Solution:
    def countVowelStrings(self, n: int) -> int:
        prev=[0]*5
        total=1
        for i in range(n):
            curr=[0]*5
            curr[0]=total
            for j in range(1,5):
                curr[j]=curr[j-1]-prev[j-1]
                total+=curr[j]
            prev=curr
        return total
''' Time Complexity--O(n*4)
    Space Complexity--O(5)'''
