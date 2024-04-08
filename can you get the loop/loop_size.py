"""loop"""
def loop_size(node):
    """loop size"""
    nodes = {}
    while True:
        if node in nodes:
            break
        else:
            nodes[node] = len(nodes)
            node = node.next
    return len(nodes) - nodes[node]
