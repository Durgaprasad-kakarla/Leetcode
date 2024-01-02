class StockSpanner:

    def __init__(self):
        self.dic={}
        self.stack=[]

    def next(self, price: int) -> int:
        cnt=1
        while self.stack and self.stack[-1]<=price:
            cnt+=self.dic[self.stack[-1]]
            self.stack.pop()
        self.dic[price]=cnt
        self.stack.append(price)
        return cnt

''' Time Comlexity--O(n)
    Space Complexity--O(n)'''


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
