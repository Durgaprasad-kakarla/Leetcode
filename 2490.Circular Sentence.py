class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s=sentence.split(" ")#Firstly we split the sentence with space as delimiter
        if sentence[0]!=sentence[-1]:#here we checked the first and last character of the string 
            return False
        for i in range(len(s)-1):#Here we checked the each word last character and next word first character in the list 's'
            if s[i][len(s[i])-1]!=s[i+1][0]:
                return False
        return True
