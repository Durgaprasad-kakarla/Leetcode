class SeatManager:

    def __init__(self, n: int):
        self.stack=[i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heapq.heappop(self.stack)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.stack,seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
''' Time Complexity--O(logn)
    Space Complexity--O(n)'''
