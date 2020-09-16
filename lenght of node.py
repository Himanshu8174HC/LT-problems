
########Driver Code On GFG
def findlen(head_Node):
    count = 0
    while head_Node:
        count += 1
        head_Node = head_Node.next
       return count
