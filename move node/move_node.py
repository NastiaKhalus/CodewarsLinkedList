"""moving a node"""
class Node(object):
    """node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """context"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """moves node"""
    if source is None:
        raise ValueError
    element = source
    source = source.next
    element.next = dest
    dest = element
    return Context(source, dest)