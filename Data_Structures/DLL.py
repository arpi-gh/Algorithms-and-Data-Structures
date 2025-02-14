class DLListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class DLL:
    def __init__(self, array: list[int]):
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__head = self.__create(array)

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    def __create(self, array: list[int]):
        if array:
            head = prev = DLListNode(array[0])
            self.__size = 1
            for i in range(1, len(array)):
                node = DLListNode(array[i])
                prev.next = node
                node.prev = prev
                prev = node
                self.__size += 1
            self.__tail = prev
        return head

    def append(self, value: int):
        node = DLListNode(value)
        self.__tail.next = node
        node.prev = self.__tail
        self.__tail = node
        self.__size += 1

    def insert(self, value, index):
        if index >= self.__size:
            self.append(value)
        else:
            current = self.__head
            cur_index = 0
            while cur_index < index-1:
                current = current.next
                cur_index += 1
            tmp = current.next
            node = DLListNode(value)
            current.next = node
            node.prev = current
            node.next = tmp
            tmp.prev = node
        self.__size += 1

    def remove(self, value):
        if self.__head.val == value:
            self.__head = self.__head.next
        elif self.__tail.val == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            prev = self.__head
            current = self.__head.next
            while current:
                if current.val == value:
                    prev.next = current.next
                    prev.next.prev = prev
                    break
                prev = current
                current = current.next
        self.__size -= 1

    def pop(self, index=None):
        popped = None
        if index == 0:
            popped = self.__head
            self.__head = self.__head.next
            self.__head.prev = None
        elif not index or index >= self.__size:
            current = self.__head
            while current.next.next:
                current = current.next
            popped = current.next
            current.next = None
            self.__tail = current
        else:
            prev = self.__head
            current = prev.next
            cur_index = 1
            while cur_index != index:
                prev = current
                current = current.next
                cur_index += 1
            popped = current
            prev.next = popped.next
            popped.next.prev = prev
        self.__size -= 1
        return popped

    def show(self):
        array = []
        current = self.__head
        while current:
            array.append(current)
            current = current.next
        return array

    def show_reverse(self):
        array = []
        current = self.__tail
        while current:
            array.append(current)
            current = current.prev
        return array

    def __repr__(self):
        arr = self.show()
        return f'{arr}'



