"""task 4"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """finds node"""
    if index < 0:
        raise ValueError
    element = node
    num = 0
    for _ in range(index + 1):
        if element is None:
            raise ValueError
        if num == index:
            return element
        num += 1
        element = element.next
