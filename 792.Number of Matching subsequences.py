class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #In this function we will check that the word is a subsequence of s
        def subsequence(word,s):
            for c in word:
                i = s.find(c)
                if i == -1:
                    return False
                else:
                    s = s[i+1:]
            return True
        dict1=Counter(words)
        print(dict1)
        count1=0
        #We will check the each word in the list of words if it is true then count it
        for i in dict1.keys():
            if subsequence(i,s)==True:
                count1+=dict1[i]
        return count1
