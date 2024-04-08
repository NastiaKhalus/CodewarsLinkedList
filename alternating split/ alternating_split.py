"""splitting list"""
class Node(object):
    """new class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    """new class"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def add(first, data):
    """add"""
    temp = first
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(data)
    return first

def alternating_split(head):
    """split"""
    if head is None or head.next is None:
        raise Exception()

    temp1 = Node()
    temp2 = Node()
    temp = head
    count = 0
    while temp is not None:
        if count % 2 == 0:
            temp1 = add(temp1, temp.data)
        else:
            temp2 = add(temp2, temp.data)
        temp = temp.next
        count += 1
    context = Context(temp1.next, temp2.next)
    return context