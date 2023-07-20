class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            stack.append(i)
            while len(stack)>1 and stack[-1]<0 and stack[-2]>0:
                if abs(stack[-1])>abs(stack[-2]):
                    stack.pop(-2)
                elif abs(stack[-1])<abs(stack[-2]):
                    stack.pop(-1)
                else:
                    stack.pop(-1)
                    stack.pop(-1)
        return stack
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
