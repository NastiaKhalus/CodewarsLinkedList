"""pairs"""
class Node:
    """new class"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """swapping pairs"""
    empty = Node()
    empty.next = head

    temp = empty
    while temp is not None and temp.next is not None and temp.next.next is not None:
        n1 = temp.next
        n2 = temp.next.next

        temp.next = n2
        n1.next = n2.next
        n2.next = n1
        temp = n1
    return empty.next
