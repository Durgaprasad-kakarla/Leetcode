class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=len(sentences[0].split(" "))
        for s in sentences:
            s=s.split(" ")
            if len(s)>max1:
                max1=len(s)
        return max1
