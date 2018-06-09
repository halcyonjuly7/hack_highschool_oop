def add_tail(list_head, val):
    current = list_head
    if current is not None:
        while current.next is not None:
            current = current.next
        current.content = val

