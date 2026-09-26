class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def detect_cycle_start(head: ListNode | None) -> ListNode | None:
    """
    Return the node where the cycle begins.
    Return None if there is no cycle.
    """
    # Phase one is to check to see if a cycle even exists
    slow = head
    fast = head
    foundCycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            foundCycle = True
            break

    if not foundCycle:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
