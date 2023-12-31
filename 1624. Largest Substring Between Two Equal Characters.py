class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic={}
        n=len(s)
        maxi=-1
        for i in range(n):
            if s[i] in dic:
                maxi=max(maxi,i-dic[s[i]]-1)
            else:
                dic[s[i]]=i
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
