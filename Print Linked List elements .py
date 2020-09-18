'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def printlist(node):
    cur = node
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    return
