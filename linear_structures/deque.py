class Deque(object):
    '''
        A basic implementation of a deque
        O(1) addition and removal from front
        O(n) addition and removal from end
    '''

    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def add_front(self, item):
        self.list.append(item)

    def add_rear(self, item):
        self.list.insert(0, item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        return self.list.pop()

    def remove_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        return self.list.pop(0)

    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

if __name__ == '__main__':
    a = Deque()
    a.add_front('a')
    a.add_front('b')
    a.add_front('c')
    a.add_rear('d')
    print(a.remove_rear())
    print(a)
