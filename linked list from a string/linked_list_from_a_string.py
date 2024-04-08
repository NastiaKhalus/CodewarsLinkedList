"""new task"""
class Node:
    """created new class"""
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """creates a list from string"""
    line = s.split('->')
    line1 = line[-2::-1]
    head = None
    for i in line1:
        head = Node(int(i),head)
    return head