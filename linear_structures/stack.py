class Stack(object):
    '''
        A basic implementation of a queue using lists
        O(1) addition, O(n) removal
    '''

    def __init__(self):
        self.list = []
        self.size = 0

    def push(self, item):
        self.list.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('stack is empty')
        self.size -= 1
        return self.list.pop(0)

    def top(self):
        if self.size == 0:
            raise IndexError('stack is empty')
        return self.list[-1]

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

if __name__ == '__main__':
    a = Stack()
    a.push('a')
    print(a.top())
    print(a.pop())
    print(a.top())