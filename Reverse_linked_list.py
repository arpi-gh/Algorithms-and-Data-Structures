def reverse_list(head: ListNode) -> ListNode:
    null = ListNode(0)
    null.next = head
    prev_head = current = head
    prev = null
    while current and current.next:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    current.next = prev
    head = current
    prev_head.next = None
    return head

#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# print(reverse_list(node1))