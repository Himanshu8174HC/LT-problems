#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    if head is None:
        return 1
    cur = head
    while head != cur.next:
        if not cur.next:
            return 0
        cur = cur.next
    return 1
