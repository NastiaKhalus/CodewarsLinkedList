"""function for convering a list"""
class Node():
    """created a new class"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """function converts list to a sting"""
    if node is None:
        return "None"
    res = str(node.data)+ " -> " + stringify(node.next)
    return res
