class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack,n=[],len(s)
        for i in range(n):
            if s[i]==')':
                st=''
                while stack and stack[-1]!='(':
                    t=stack.pop()
                    if len(t)>1:
                        t=t[::-1]
                    st+=t
                stack.pop()
                stack.append(st)
            else:
                stack.append(s[i])
            # print(stack)
        return "".join(stack)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
