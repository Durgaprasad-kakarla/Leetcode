class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        lst=[]
        lst.append(words[0])
        for i in range(1,n):
            if groups[i]!=groups[i-1]:
                lst.append(words[i])
        return lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
