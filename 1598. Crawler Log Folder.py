class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n,lst=len(logs),[]
        n=len(logs)
        for i in range(n):
            if logs[i]=="../":
                if lst:
                    lst.pop()
            elif logs[i]=='./':
                continue
            else:
                lst.append(logs[i])
        return len(lst)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
