"""reversing"""
class Node(object):
    """new class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """reversing nodes"""
    if head is None or head.next is None:
        return head
    new = reverse(head.next)
    head.next.next = head
    head.next = None
    return new