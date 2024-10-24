class MyQueue:

    def __init__(self):
        self.s=[]
        

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = []
        ans = None
        # Move elements from s to temp, except for the front element
        while len(self.s) > 1:
            temp.append(self.s.pop())
        # The last element in s is the front of the queue
        if self.s:
            ans = self.s.pop()  # Get the front element (FIFO behavior)
        # Move the elements back to s
        while temp:
            self.s.append(temp.pop())
        return ans

    def peek(self) -> int:
        temp = []
        ans = None
        # Move elements from s to temp, except for the front element
        while len(self.s) > 1:
            temp.append(self.s.pop())
        # The last element in s is the front of the queue
        if self.s:
            ans = self.s[-1]  # Get the front element (FIFO behavior)
        # Move the elements back to s
        while temp:
            self.s.append(temp.pop())

        return ans

    def empty(self) -> bool:
        return len(self.s)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()