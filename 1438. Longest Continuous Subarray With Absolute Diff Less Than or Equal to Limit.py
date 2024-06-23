class Solution:
    def longestSubarray(self, a: List[int], limit: int) -> int:
        mindeque=deque()
        maxdeque=deque()
        n=len(a)
        pos=0
        for i in range(n):
            while maxdeque and a[i]>maxdeque[-1]:
                maxdeque.pop()
            while mindeque and a[i]<mindeque[-1]:
                mindeque.pop()
            maxdeque.append(a[i])
            mindeque.append(a[i])
            if maxdeque[0]-mindeque[0]>limit:
                if maxdeque[0]==a[pos]:
                    maxdeque.popleft()
                if mindeque[0]==a[pos]:
                    mindeque.popleft()
                pos+=1
        return n-pos
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
