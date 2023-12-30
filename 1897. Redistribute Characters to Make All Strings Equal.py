class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s=''.join(words)
        n=len(words)
        if len(s)%len(words)!=0:
            return False
        else:
            dic=Counter(s)
            for i in dic:
                if dic[i]%n!=0:
                    return False
            return True
''' Time Complexity--O(n*k)-(length of words--k)
    Space Complexity--O(n*k)'''
