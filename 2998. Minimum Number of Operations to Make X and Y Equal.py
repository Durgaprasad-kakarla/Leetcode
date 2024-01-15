class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        vis=set()
        queue=deque([(x,0)])
        vis.add(x)
        while queue:
            num,turn=queue.popleft()
            if num==y:
                return turn
            if num+1 not in vis:
                queue.append((num+1,turn+1))
                vis.add(num+1)
            if num-1>=0 and num-1 not in vis:
                queue.append((num-1,turn+1))
                vis.add(num-1)
            if num%11==0 and num//11 not in vis:
                queue.append((num//11,turn+1))
                vis.add(num//11)
            if num%5==0 and num//5 not in vis:
                queue.append((num//5,turn+1))
                vis.add(num/11)
        return -1
''' Time Complexity--O(max(x,y))
    Space Complexity--O(max(x,y))
