class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if stack1 and s[i]=="#":
                stack1.pop(-1)
            elif s[i]!='#':
                stack1.append(s[i])
        for i in range(len(t)):
            if stack2 and t[i]=="#":
                stack2.pop(-1)
            elif t[i]!='#':
                stack2.append(t[i])
        return stack1==stack2
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
