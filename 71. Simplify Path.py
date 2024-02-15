class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        s=''
        path=path+'/'
        for i in path:
            if i!='/':
                s+=i
            else:
                if s=="..":
                    if stack:
                        stack.pop()
                elif s!='' and s!='.':
                    stack.append(s)
                s=''
        return '/'+'/'.join(stack)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
