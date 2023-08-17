class Solution:
    def addMinimum(self, word: str) -> int:
        stack=[]
        count_operations=0
        for i in word:
            #if stack is empty
            if not stack:
                stack.append(i)
            #if peak element is less than the element from word i then append it to stack
            elif stack and ord(stack[-1])<ord(i):
                stack.append(i)
            #if stack is not empty and peak element is greater than the element from word then add number of elements needed to get 'abc' i.e., 3-len(stack) empty the stack and append i
            elif stack and ord(stack[-1])>=ord(i):
                count_operations+=(3-len(stack))
                stack=[]
                stack.append(i)
            #if len(stack)==3 means we have 'abc' in the stack so make stack empty and count is zero.
            if len(stack)==3:
                stack=[]
        return count_operations+(3-len(stack)) if stack else count_operations
''' Time Complexity--O(n)
    space Complexity--O(3)'''
