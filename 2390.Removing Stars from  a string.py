class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="*":#if * appears then remove the previous element in the stack
                stack.pop()
            else:#else append the element to the stack
                stack.append(i)
        return ''.join(stack)#Finally join all the elements in the stack
