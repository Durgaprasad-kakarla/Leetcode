class Solution:
    def canReach(self, s: str, minjump: int, maxjump: int) -> bool:
        queue=deque([0])
        maxi=0
        n=len(s)
        while queue:
            ele=queue.popleft()
            if ele==n-1:
                return True
            for i in range(max(ele+minjump,maxi+1),min(n,ele+maxjump+1)):
                if  s[i]=='0':
                    queue.append(i)  
            maxi=ele+maxjump
        return False
''' Time Complexity--O(n)
    Space Complexity--O(n)
