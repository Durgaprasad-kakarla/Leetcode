class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1=Counter(s)
        dict2=Counter(t)
        count=0
        for i in dict1.keys():
            if not dict2[i]:
                count+=dict1[i]
            else:
                count+=abs(dict1[i]-dict2[i])
        for i in dict2.keys():
            if not dict1[i]:
                count+=dict2[i]
        return count
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
