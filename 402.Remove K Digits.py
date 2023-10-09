class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n=len(num)
        for i in range(n):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop(-1)
                k-=1
            stack.append(num[i])
        while stack and stack[0]=='0':
            stack.pop(0)
        while stack and k>0:
            stack.pop(-1)
            k-=1
        if not stack:
            return "0"
        return "".join(stack)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
