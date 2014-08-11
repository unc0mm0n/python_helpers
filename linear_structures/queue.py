class Queue(object):
    '''
        A basic implementation of a queue using lists
        O(1) addition, O(n) removal
    '''

    def __init__(self):
        self.list = []
        self.size = 0

    def enqueue(item):
        self.list.append(item)
        self.size += 1

    def dequeue():
        self.size -= 1
        return self.list.pop(0)

    def is_empty():
        return self.size == 0

    def size():
        return self.size