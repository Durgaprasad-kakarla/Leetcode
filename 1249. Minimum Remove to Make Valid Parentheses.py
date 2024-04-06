class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            if s[i]==')':
                while stack and stack[-1][0].isalpha():
                    stack.pop()
                if stack and stack[-1][0]=='(':
                    stack.pop()
                else:
                    stack.append([')',i])
            elif s[i]=='(':
                stack.append([s[i],i])
        s=list(s)
        for _,i in stack:
            if s[i]==')' or s[i]=='(':
                s[i]=''
        return "".join(s)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
