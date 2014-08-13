from collections import deque

class Queue(object):
    '''
        A basic implementation of a queue using a Deque
        O(1) addition and removal

        enqueue(self, item) => Add an item to back of the queue
        dequeue(self, item) => Remove an item from the front of the queue, raise IndexError if empty
        is_empty(self) => return True if empty
        __len__(self) => return the number of elements in the queue
    '''

    def __init__(self):
        self.items = deque()

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

if __name__ == '__main__':
    a = Queue()
    a.enqueue('a')
    a.enqueue('b')
    a.enqueue('c')
    a.enqueue('d')
    print(a.dequeue())
    print(a.dequeue())
    print(len(a), a.is_empty())
    print(a.dequeue())
    print(a.dequeue())
    print (a.is_empty())