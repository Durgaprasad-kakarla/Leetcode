class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        problem_letters=[]
        dic=Counter(s)
        valid=True
        for i in dic:
            if dic[i]<k:
                problem_letters.append(i)
                valid=False
        if valid:
            return len(s)
        for i in problem_letters:
            s=s.replace(i," ")
        splitted_str=s.split(" ")
        maxi=0
        for st in splitted_str:
            maxi=max(maxi,self.longestSubstring(st,k))
        return maxi
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
