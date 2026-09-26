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


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum equals k.
    """
    current_sum = 0
    starts = {0: 1}
    count = 0
    for num in nums:
        current_sum += num
        difference = current_sum - k
        if difference in starts:
            count += starts[difference]
        starts[difference] = starts.get(difference, 0) + 1

    return count


def last_occurrence(nums: list[int], target: int) -> int:
    """
    nums is sorted.
    Return the last index containing target,
    or -1 if target does not exist.
    """
    right = 0
    left = 0
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid
            result = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
