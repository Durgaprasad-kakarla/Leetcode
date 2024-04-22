class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends or target in deadends:
            return -1
        lock=target
        cnt1,cnt2=0,0
        deadends=set(deadends)
        queue=deque()
        queue.append([0,'0000'])
        vis=set()
        while queue:
            d,lock=queue.popleft()
            if lock==target:
                return d
            for i in range(4):
                forward=int(lock[i])+1
                if forward==10:
                    st1=lock[:i]+str(0)+lock[i+1:]
                else:
                    st1=lock[:i]+str(forward)+lock[i+1:]
                if st1 not in deadends and st1 not in vis:
                    queue.append([d+1,st1])
                    vis.add(st1)
                backward=int(lock[i])-1
                if backward==-1:
                    st2=lock[:i]+str(9)+lock[i+1:]
                else:
                    st2=lock[:i]+str(backward)+lock[i+1:]
                if st2 not in deadends and st2 not in vis:
                    queue.append([d+1,st2])
                    vis.add(st2)
        return -1
''' Time Complexity--O((n^4)*n*len(deadends))-->n is 10 digits
    Space Complexity--O(n^4)'''
