class Queue(object):
    '''
        A basic implementation of a queue using lists
        O(1) addition, O(n) removal
    '''

    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

if __name__ == '__main__':
    a = Queue()
    a.enqueue('a')
    a.enqueue('b')
    a.enqueue('c')
    a.enqueue('d')
    print(a.dequeue())
    print(a.dequeue())
    print(a.size(), a.is_empty())
    print(a.dequeue())
    print(a.dequeue())
    print (a.is_empty())