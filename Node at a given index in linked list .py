####################SEE GFG Driver code

def getNth(head, k):
    while k-1:
        head=head.next
        k-=1
    return head.data
