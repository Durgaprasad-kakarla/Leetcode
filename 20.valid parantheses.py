class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={')':'(','}':'{',']':'['}
        for p in s:
            if p in closetoopen.values():
                stack.append(p)
            elif stack and closetoopen[p]==stack[-1]:
                value=stack.pop()
            else:
                return False
        if stack==[]:
            return True
