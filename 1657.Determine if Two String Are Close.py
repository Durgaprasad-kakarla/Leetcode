class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1=Counter(word1)#dictionary with the count of their characters in dict1 and dict2
        dict2=Counter(word2)
        if sorted(dict1.values())==sorted(dict2.values()) and sorted(set(word1))==sorted(set(word2)):#Now check that the counts of two words characters are same and characters should be same in both the words
            return True
        return False
