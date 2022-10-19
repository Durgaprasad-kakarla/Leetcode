class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence=set(sentence)
        if len(sentence)<26:
            return False
        return True
