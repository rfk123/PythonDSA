
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(5)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(1)
head1.next.next.next.next.next = ListNode(0)


head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(1)
head2.next.next.next.next = ListNode(0)


def get_intersection_node(headA: ListNode | None, headB: ListNode | None) -> ListNode:
    listA = headA
    listB = headB

    while listA != listB:
        listA = listA.next if listA else headB
        listB = listB.next if listB else headA

    return listA


print(get_intersection_node(head1, head2))
