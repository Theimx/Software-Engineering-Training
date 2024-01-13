class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue size:", my_queue.size())
print("Front element:", my_queue.front())

while not my_queue.is_empty():
    print("Dequeue:", my_queue.dequeue())

print("Queue size after dequeue:", my_queue.size())

Queue Implementation in Python

1. Introduction:
   The Queue is a fundamental data structure that follows the First-In-First-Out (FIFO) principle. It is used to store and manage a collection of elements, where the first element added is the first to be removed.

2. Class Definition:
   The Queue class is implemented in Python with the following methods:

   - __init__(self): Initializes an empty queue.

   - is_empty(self): Returns True if the queue is empty; otherwise, returns False.

   - enqueue(self, item): Adds the specified item to the end of the queue.

   - dequeue(self): Removes and returns the front element from the queue. Raises an IndexError if the queue is empty.

   - front(self): Returns the front element of the queue without removing it. Raises an IndexError if the queue is empty.

   - size(self): Returns the number of elements in the queue.

3. Example Usage:
   ```python
   # Create a new Queue
   my_queue = Queue()

   # Enqueue elements
   my_queue.enqueue(1)
   my_queue.enqueue(2)
   my_queue.enqueue(3)

   # Access front element
   front_element = my_queue.front()
   print("Front element:", front_element)

   # Dequeue elements
   while not my_queue.is_empty():
       dequeued_element = my_queue.dequeue()
       print("Dequeue:", dequeued_element)

   # Check queue size after dequeue
   print("Queue size after dequeue:", my_queue.size())
