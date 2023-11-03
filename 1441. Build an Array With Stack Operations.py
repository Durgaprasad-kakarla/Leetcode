class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        p,x=0,len(target)
        lst,stack=[],[]
        for i in range(1,n+1):
            lst.append("Push")
            stack.append(i)
            if stack and stack[-1]==target[p]:
                p+=1
                if x==p:
                    return lst
            else:
                if stack:
                    lst.append("Pop")
                    stack.pop()
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
