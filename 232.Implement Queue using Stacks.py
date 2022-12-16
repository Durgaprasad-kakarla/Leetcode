class MyQueue:

    def __init__(self):
        #Take two stacks for implementing a Queue
        self.s1=[]
        self.s2=[]        

    def push(self, x: int) -> None:
        #Push element into the queue
        while self.s1:
            self.s2.append(self.s1.pop())#if s1 is not empty then append top element of s1 into s2
        self.s1.append(x)#append the x into s1 stack
        while self.s2:
            self.s1.append(self.s2.pop())#if s2 is not empty then append the top element of s2 into s1

    def pop(self) -> int:
        #Popping the element from queue
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]#returns top element of the s1 

    def empty(self) -> bool:
        return not self.s1#checks s1 is empty or not


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
