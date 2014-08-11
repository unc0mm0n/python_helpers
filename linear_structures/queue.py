class Queue(object):
    '''
        A basic implementation of a queue using lists
        O(1) addition, O(n) removal
    '''

    def __init__(self):
        self.list = []
        self.size = 0

    def enqueue(self, item):
        self.list.append(item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.list.pop(0)

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size