class Stack(object):
    '''
        A basic implementation of a stack using lists
        O(1) addition, O(1) removal
    '''

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.list.pop()

    def top(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.list[-1]

    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

if __name__ == '__main__':
    a = Stack()
    a.push('a')
    a.push('b')
    a.push('c')
    print(a.top())
    print(a.pop())
    try:
        print(a.top())
    except IndexError:
        print('yey, excepted!')
