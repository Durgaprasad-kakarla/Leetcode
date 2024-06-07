class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        st=set(dictionary)
        sentence=list(sentence.split(" "))
        for i in range(len(sentence)):
            for j in range(len(sentence[i])):
                if sentence[i][:j] in st:
                    sentence[i]=sentence[i][:j]
        return " ".join(sentence)
''' Time Complexity--O(n*n)
    Space Complexity--O(1)'''
