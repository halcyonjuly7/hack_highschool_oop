# class Node:
#     def __init__(self, item):
#         self._content = item
#
#     def

class LinkedList:
    class Node:
        def __init__(self, item):
            self._content = item
            self._next = None


        def __repr__(self):
            return f"Node<{self.content}>"


        @property
        def content(self):
            return self._content

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, next_node):
            self._next = next_node


    def __init__(self):
        self._head = None
        self._tail = None

    def __iter__(self):
        current_item  = self.head
        while current_item is not None:
            yield current_item
            current_item = current_item.next


    @property
    def front(self):
        return self._head

    @property
    def tail(self):
        return self._tail



    def add_head(self, item):
        new_node = LinkedList.Node(item)
        if self.front is None:
            self._tail = self._head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_tail(self, item):
        new_node = LinkedList.Node(item)
        if self.front is None:
            self._tail = self._head = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node



    def add(self, item):
        self.add_tail(item)


#
# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.add_tail(1)
#     ll.add_tail(2)
#
#     for i in ll:
#         print(i)



