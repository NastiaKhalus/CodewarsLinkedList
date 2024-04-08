"""functions"""
class Node(object):
    """new class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """sorted"""
    new = Node(data)
    if head is None:
        new.next = head
        return new
    temp = head
    while temp.next is not None and temp.next.data < data:
        temp = temp.next
    new.next = temp.next
    temp.next = new
    return head
