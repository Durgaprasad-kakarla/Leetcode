class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        m=len(popped)
        stack=[]
        i,j=0,0
        while i<=n and j<m:
            if stack!=[] and stack[-1]==popped[j]:
                stack.pop(-1)
                j+=1
            else:
                if i==n:
                    return False
                stack.append(pushed[i])
                i+=1
        return True
''' Time Complexity--O(n)
    Space Compexity--O(n)'''
