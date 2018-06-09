def insertion_sort(current_node, unsorted_list):
    for node in unsorted_list:
        if current_node.content < node.content:
            tmp = node.content
            node.content = current_node.content
            current_node.content = tmp

def sort_asc(unsorted_list):
    current = unsorted_list.next
    while current is not None:
        next_node = current.next 
        insertion_sort(current, unsorted_list)
        current = next_node
