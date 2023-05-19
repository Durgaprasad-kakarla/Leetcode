class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=Counter(ransomNote)
        dict2=Counter(magazine)
        for i in dict1:
            if dict1[i]:
                if dict1[i]>dict2[i]:
                   return False
            else:
                return False
        return True
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
