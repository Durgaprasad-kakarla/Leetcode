class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic=Counter(chars)
        tot=0
        for word in words:
            worddic=Counter(word)
            n=len(worddic)
            cnt=0
            for i in worddic:
                if i in dic:
                    if dic[i]>=worddic[i]:
                        cnt+=1
            if cnt==n:
                tot+=len(word)
        return tot
''' Time Complexity--O(n*len(word))
    Space Complexity--O(len(chars))'''
