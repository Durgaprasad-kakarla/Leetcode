class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count=[0]*1024
        count[0]=1
        ans=0
        mask=0
        for ch in word:
            mask=mask^(1<<(ord(ch)-ord('a')))
            ans+=count[mask]
            for i in range(10):
                ans+=count[mask^1<<i]
            count[mask]+=1
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
