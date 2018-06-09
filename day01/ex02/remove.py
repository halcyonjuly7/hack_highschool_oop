
def remove(list_head, val):
    current = list_head
    prev = None
    while current is not None:
        if current.content == val:
            prev.next = current.next
            break
        prev = current
        current = current.next


def stuff(a):
    a 


if __name__ == "__main__":
    pass
