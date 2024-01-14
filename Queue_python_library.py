# Creating Queue using python 

from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()

# enqueuing data in Queue.

    def enqueue(self,data):
        self.queue.append(data)

# checking if Queue is Empty.

    def isEmpty(self):
        return len(self.queue)==0

# checking peek element.

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "Queue is Empty."

# Dequeueing element from Queue.

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.popleft()
        else:
            return "Queue is Empty."

# Checking size of elements

    def size(self):
        print(len(self.queue))



# Main function

if __name__=='__main__':
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(13)
    queue.enqueue(115)
    queue.enqueue(16)
    print(list(queue.queue))
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
