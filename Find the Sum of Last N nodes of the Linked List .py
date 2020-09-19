list1 = []
    while head is not None:
        list1.append(head.data)
        head = head.next
    return sum(list1[-n:])
############################ REVERSE AND SUM
curr_node = head
prev = None
while curr_node:
temp = curr_node.next
curr_node.next = prev
prev = curr_node
curr_node = temp
head = prev

result = 0
while n:
result += head.data
head = head.next
n -= 1

return result
