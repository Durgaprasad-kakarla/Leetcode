class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic={0:-1}
        cnt,maxi=0,0
        n=len(s)
        for i in range(n):
            if s[i] in "aeiou":
                cnt^=(1<<(ord(s[i])-97))
            if cnt in dic:
                maxi=max(maxi,i-dic[cnt])
            else:
                dic[cnt]=i
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(`)
