class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue=[]
        queue.append([beginWord,1])
        wordset={word for word in wordList}
        while queue:
            x=queue.pop(0)
            word=x[0]
            steps=x[1]
            if word==endWord:
                return steps
            word=list(word)
            for i in range(len(word)):
                original=word[i]
                for ch in range(97,123):
                    word[i]=chr(ch)
                    if "".join(word) in wordset:
                        wordset.remove("".join(word))
                        queue.append(["".join(word),steps+1])
                word[i]=original
        return 0
''' Time Complexity--O(26*n*wordlength*logn)-->26 letter will be checked--n(number of words)--wordlength(length of each word)--logn(for checking the word in set)
    Space Complexity--O(n)'''
