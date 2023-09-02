#LC 225 Implement a stack data structure using a queue

class MyStack:

    #initialize the queue data structure
    def __init__(self):
        self.q = self.collections.deque()

    #just a normal append operation. We're putting it in the end of the queue
    def push(self, x: int) -> None:
        self.q.append(x)

    #we wanna pop every value except the last one. Get the value we're looking for, and re-append everything we popped
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    #return the right most index which would be the most recent value
    def top(self) -> int:
        return self.q[-1]
    
    #check to see if there's anything in the queue
    def empty(self) -> bool:
        return len(self.q) == 0