class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n=len(words)
        def maxScore(ind,dic):
            if ind==n:
                return 0
            word=words[ind]
            dc=Counter(word)
            s=0
            flag=0
            l=maxScore(ind+1,dic)
            for i in word:
                if i not in dic or dc[i]>dic[i]:
                    flag=1
                    break
            r=0
            if flag==0:
                for i in word:
                    s+=score[ord(i)-97]
                    dic[i]-=1
                r=s+maxScore(ind+1,dic)
                for i in word:
                    dic[i]+=1
            return max(l,r)
        dic=Counter(letters)
        return maxScore(0,dic)
''' Time Complexity--O(2^n*len(word))
    Space Complexity--O(letters)'''
