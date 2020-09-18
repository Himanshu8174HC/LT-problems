def areIdentical(head1, head2):
    count1 = 0
    cur_1 =head1
    while cur_1:
        count1+=1
        cur_1=cur_1.next

    count2 = 0
    cur_2 =head2
    while cur_2:
        count2 += 1
        cur_2=cur_2.next

    if count1 != count2:
        return False
    cur_1 =head1
    cur_2 =head2
    while cur_1:
        if cur_1.data != cur_2.data:
            return False
        cur_1 = cur_1.next
        cur_2 = cur_2.next
    return True
