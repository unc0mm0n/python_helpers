class LinkedList(object):

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = next

        def set_next(self, other):
            self.next = other

        def get_next(self):
            return self.next

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data

    def __init__(self):
        self.head = None

    def __str__(self):
        str = ''
        current = self.head
        while current != None:
            str += '{0}, '.format(current.get_data())
            current = current.get_next()
        return str


    def add(self, item):
        self.head, tmp = self.Node(item), self.head
        self.head.set_next(tmp)

    def remove(self, item):
        prev = None
        current = self.head
        while current != None:
            if current.get_data() == item:

                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True
            prev = current
            current = current.get_next()
        return False

    def pop(self):
        if self.head:
            tmp = self.head
            self.head = self.head.get_next()
            return tmp.get_data()
        return None



if __name__ == '__main__':
    a = LinkedList()
    a.add(1)
    print(a.pop())
    print(a.pop())
    print('yey')
    print(a)
