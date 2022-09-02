class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l=s.count(letter)
        return int((l/len(s))*100)
