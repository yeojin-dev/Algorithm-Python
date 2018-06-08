class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:

    def __init__(self, data=None):
        self._head = Node(data)
        self._size = 1 if data else 0

    def __len__(self):
        return self._size

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= self._size:
            raise StopIteration
        curr_node = self[self._index]
        self._index += 1
        return curr_node

    def __getitem__(self, item):
        if item > self._size:
            raise ValueError
        result = self._head
        for i in range(item):
            result = result.next
        return result

    def append(self, data):
        new_node = Node(data)
        curr_node = self._head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        self._size += 1

    def insert(self, index, data):
        if index > self._size:
            raise ValueError

        new_node = Node(data)
        curr_node = self._head

        if index == 0:
            new_node.next = self._head
            self._head = new_node

        else:
            for i in range(index - 1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node

        self._size += 1

    def delete(self, index):
        if index > self._size:
            raise ValueError

        curr_node = self[index - 1]
        curr_node.next = self[index].next
        self._size -= 1

    def pop(self):
        result = self[self._size - 1].data
        self.delete(self._size - 1)
        return result
