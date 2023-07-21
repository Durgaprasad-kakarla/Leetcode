class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        max_val=0
        dictionary=defaultdict(int)
        for word in words:
            for l in word:
                dictionary[word]=dictionary[word]|(1<<(ord(l)-97))
        for word1,word2 in combinations(dictionary.keys(),2):
            if dictionary[word1]&dictionary[word2]==0:
                max_val=max(max_val,len(word1)*len(word2))
        return max_val
''' Time Complexity--O(n^2)
    Space Complexity--O(n)'''
