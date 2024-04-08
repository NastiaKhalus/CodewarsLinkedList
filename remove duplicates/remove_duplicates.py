"""removing duplicates"""
class Node(object):
    """new class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """function removes duplicates"""
    temp = head
    while temp is not None and temp.next is not None :
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
