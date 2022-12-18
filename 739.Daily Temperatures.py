class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []#index and temp
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:#if the stack is not empty and t is greater than stack[-1][0]
                stackt,stackind=stack.pop()#pop the element
                res[stackind]=(i-stackind)#result will be stored with difference of i and stackind
            stack.append([t,i])#append the [t,i]
        return res
