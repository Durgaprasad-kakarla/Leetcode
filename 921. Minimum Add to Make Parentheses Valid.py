class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        n=len(s)
        for i in range(n):
            if stack and stack[-1]=='(' and s[i]==')':
                stack.pop(-1)
            else:
                stack.append(s[i])
        return len(stack)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
