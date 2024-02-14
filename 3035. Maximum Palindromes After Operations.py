class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        wordsize=[]
        for w in words:
            wordsize.append(len(w))
        wordsize.sort()
        freq={}
        for w in words:
            for c in w:
                if c in freq:
                    freq[c]+=1
                else:
                    freq[c]=1
        even,odd=0,0
        n=len(wordsize)
        for p in freq:
            even+=freq[p]//2
            odd+=freq[p]%2
        ans=0
        for i in range(n):
            if wordsize[i]%2:
                if odd:
                    odd-=1
                else:
                    even-=1
                    odd+=1
            if even<wordsize[i]//2:
                break
            even-=wordsize[i]//2
            ans+=1
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
