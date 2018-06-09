class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._end = None


    def is_empty(self):
        return self._head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self._head is None:
            self._end = self._head = new_node
        else:
            self._end.next(new_node)
            self._end = new_node
        self._size += 1
    
    def dequeue(self):
        if not self.is_empty():
            self._size -= 1
            node = self._head
            self._head = self._head.next
            return node

    def front(self):
        return self._head

    def __str__(self):
        items = []
        current = self._head
        while current is not None:
            items.append(current.val)
            current = current.next
        return items


