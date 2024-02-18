class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count, free, taken = [0] * n, list(range(n)), []
        heapq.heapify(free)    
        meetings.sort()
        prev = -1
        
        for start, end in meetings:
            duration = end - start
            start = max(start, prev)
            end = start + duration
            
            while taken and taken[0][0] <= start:
                _, i = heapq.heappop(taken)
                heapq.heappush(free, i)
            
            if not free:
                start = taken[0][0]
                end = start + duration
                while taken and taken[0][0] <= start:
                    _, i = heapq.heappop(taken)
                    heapq.heappush(free, i)
            
            i = heapq.heappop(free)
            count[i] += 1
            heapq.heappush(taken, [end, i])
            
            prev = start
            
        return count.index(max(count))
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
