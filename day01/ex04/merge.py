
def merge(train1, train2):
    current = train1
    if train1 is not None:
        while current.next is not None:
            current = current.next
        current.next = train2
    return train1
