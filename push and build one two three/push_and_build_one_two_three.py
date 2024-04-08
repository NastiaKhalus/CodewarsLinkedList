"""push and build"""
class Node:
    """created a new class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """function pushes objects"""
    new = Node(data)
    if head is None:
        return new
    new.next = head
    return new

def build_one_two_three():
    """builds linked list"""
    return push(push(push(None, 3), 2), 1)