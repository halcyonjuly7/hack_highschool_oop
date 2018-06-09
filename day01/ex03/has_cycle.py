def has_cycle(list_head):
    if list_head:
        head = next(list_head)
        for node in list_head:
            if head == node:
                return True
    return False
