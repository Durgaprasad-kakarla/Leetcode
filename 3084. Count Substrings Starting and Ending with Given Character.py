class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt=0
        for i in range(len(s)):
            if s[i]==c:
                cnt+=1
        return (cnt*(cnt+1))//2
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
