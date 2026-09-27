
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if not list2 else list2
    print(output_list(dummy.next))
    return dummy.next


head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(5)
head1.next.next.next.next = ListNode(7)
# 1 -> 3 -> 3 -> 5 -> 7 -> None

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
# head2.next.next.next = ListNode(1)
# head2.next.next.next.next = ListNode(1)
# head2.next.next.next.next.next = ListNode(0)
# 0 -> 2 -> 2 -> 6 -> 6 -> 15 -> None


def output_list(node: ListNode) -> str:
    result = ""
    while node:
        result += f"{node.val} -> "
        node = node.next
    result += "None"
    return result


# merge_two_lists(head1, head2)
# 0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 5 -> 6 -> 6 -> 7 -> 15 -> None


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    # This solution may not work if n is the same size of the linked list
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    for i in range(n + 1):
        if not fast:
            return -1
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    print(output_list(dummy.next))
    return dummy.next


# remove_nth_from_end(head2, 1)
# 0 -> 2 -> 2 -> 6 -> 6 -> 15 -> None


def is_palindrome(head: ListNode | None) -> bool:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    reversed = reverse_list(slow.next)
    node = head

    while reversed:
        if node.val != reversed.val:
            return False
        node = node.next
        reversed = reversed.next

    return True


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    node = head
    while node:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev


print(is_palindrome(head2))
